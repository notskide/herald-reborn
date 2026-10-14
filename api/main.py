"""Herald API — lightweight OpenAI-compatible gateway for Wispbyte.

This service does not contain model weights. It authenticates client requests,
translates the public Herald model names to configured upstream model IDs, and
forwards chat-completion requests to an OpenAI-compatible backend.
"""
from __future__ import annotations

import os
import secrets
from typing import Any

import httpx
from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict, Field

APP_VERSION = "0.1.0"
SERVICE_NAME = "herald-api"

app = FastAPI(
    title="Herald API",
    version=APP_VERSION,
    description=(
        "A lightweight API gateway for the Herald model family. "
        "Configure an OpenAI-compatible upstream model backend using environment variables."
    ),
)


class ChatCompletionRequest(BaseModel):
    """OpenAI-compatible chat request; unknown options pass through upstream."""

    model_config = ConfigDict(extra="allow")

    model: str = Field(..., description="Public Herald model ID")
    messages: list[dict[str, Any]] = Field(..., min_length=1)
    stream: bool = False


def configured_model_ids() -> dict[str, str]:
    """Return public Herald model names mapped to upstream model IDs."""
    return {
        "herald-core": os.getenv("HERALD_CORE_UPSTREAM_MODEL", "").strip(),
        "herald-sentinel": os.getenv("HERALD_SENTINEL_UPSTREAM_MODEL", "").strip(),
    }


def upstream_base_url() -> str:
    """Base URL must include any API prefix, e.g. https://provider.example/v1."""
    return os.getenv("HERALD_UPSTREAM_BASE_URL", "").strip().rstrip("/")


def upstream_timeout_seconds() -> float:
    try:
        return max(1.0, min(float(os.getenv("HERALD_UPSTREAM_TIMEOUT_SECONDS", "60")), 300.0))
    except (TypeError, ValueError):
        return 60.0


def error_response(status_code: int, message: str, error_type: str = "api_error") -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={"error": {"message": message, "type": error_type}},
    )


async def require_api_key(authorization: str | None = Header(default=None)) -> None:
    """Require a Bearer key. The shared key is for private testing only."""
    expected = os.getenv("HERALD_API_KEY", "").strip()
    if not expected:
        raise HTTPException(
            status_code=503,
            detail="Herald API authentication is not configured on the server.",
        )

    scheme, separator, supplied = (authorization or "").partition(" ")
    if not separator or scheme.lower() != "bearer" or not supplied.strip():
        raise HTTPException(status_code=401, detail="A Bearer API key is required.")

    if not secrets.compare_digest(supplied.strip(), expected):
        raise HTTPException(status_code=401, detail="Invalid API key.")


@app.exception_handler(HTTPException)
async def http_exception_handler(_request, exc: HTTPException) -> JSONResponse:
    if exc.status_code == 401:
        error_type = "authentication_error"
    elif exc.status_code == 400:
        error_type = "invalid_request_error"
    elif exc.status_code == 503:
        error_type = "service_unavailable_error"
    else:
        error_type = "api_error"
    return error_response(exc.status_code, str(exc.detail), error_type)


@app.get("/", tags=["status"])
async def root() -> dict[str, str]:
    return {
        "service": SERVICE_NAME,
        "version": APP_VERSION,
        "status": "running",
        "health": "/health",
        "models": "/v1/models",
        "chat_completions": "/v1/chat/completions",
    }


@app.get("/health", tags=["status"])
async def health() -> dict[str, Any]:
    base_configured = bool(upstream_base_url())
    model_map = configured_model_ids()
    return {
        "status": "ok",
        "service": SERVICE_NAME,
        "version": APP_VERSION,
        "upstream_configured": base_configured,
        "models": {
            public_name: bool(base_configured and upstream_id)
            for public_name, upstream_id in model_map.items()
        },
    }


@app.get("/v1/models", tags=["models"])
async def list_models(_: None = Depends(require_api_key)) -> dict[str, Any]:
    base = upstream_base_url()
    models = configured_model_ids()
    available = [name for name, upstream_id in models.items() if base and upstream_id]
    return {
        "object": "list",
        "data": [
            {"id": name, "object": "model", "created": 0, "owned_by": "herald-reborn"}
            for name in available
        ],
    }


@app.post("/v1/chat/completions", tags=["chat"])
async def chat_completions(
    body: ChatCompletionRequest,
    _: None = Depends(require_api_key),
) -> JSONResponse:
    public_model = body.model.strip()
    model_map = configured_model_ids()
    if public_model not in model_map:
        return error_response(
            400,
            "Unknown model. Use herald-core or herald-sentinel.",
            "invalid_request_error",
        )

    base_url = upstream_base_url()
    upstream_model = model_map[public_model]
    if not base_url or not upstream_model:
        return error_response(
            503,
            f"{public_model} is not configured with an upstream model backend yet.",
            "service_unavailable_error",
        )

    if body.stream:
        return error_response(
            400,
            "Streaming is not supported by this initial Herald API version; set stream=false.",
            "invalid_request_error",
        )

    # Preserve common provider options, but replace the public alias with the
    # provider-specific model ID. Do not log prompts, API keys, or provider bodies.
    payload = body.model_dump(exclude_none=True)
    payload["model"] = upstream_model

    headers = {"Content-Type": "application/json"}
    upstream_key = os.getenv("HERALD_UPSTREAM_API_KEY", "").strip()
    if upstream_key:
        headers["Authorization"] = f"Bearer {upstream_key}"

    endpoint = f"{base_url}/chat/completions"
    try:
        async with httpx.AsyncClient(timeout=upstream_timeout_seconds()) as client:
            response = await client.post(endpoint, json=payload, headers=headers)
    except httpx.TimeoutException:
        return error_response(504, "The upstream model request timed out.", "upstream_timeout")
    except httpx.RequestError:
        return error_response(502, "Could not connect to the upstream model backend.", "upstream_error")

    if response.status_code >= 400:
        # Do not disclose provider error bodies, which may contain internal details.
        return error_response(502, "The upstream model backend rejected or failed the request.", "upstream_error")

    try:
        result = response.json()
    except ValueError:
        return error_response(502, "The upstream backend returned a non-JSON response.", "upstream_error")

    return JSONResponse(content=result, status_code=response.status_code)


if __name__ == "__main__":
    import uvicorn

    # Wispbyte provides a public port. PORT is common; SERVER_PORT is included
    # as a fallback for server images that expose that variable instead.
    port_value = os.getenv("PORT") or os.getenv("SERVER_PORT") or "8080"
    try:
        port = int(port_value)
    except ValueError:
        raise SystemExit("PORT/SERVER_PORT must be an integer")

    uvicorn.run(app, host="0.0.0.0", port=port)
