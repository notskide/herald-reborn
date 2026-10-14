# Connect a script to Herald Reborn

This guide is for **developers using Herald from their own projects**. You do not need to host the Herald API yourself.

Herald's API is a hosted HTTP service. Your script sends a request to the API, the API routes it to a configured model backend, and your script receives the model's response.

> **Prototype status:** replace HERALD_API_BASE_URL with the real public HTTPS URL once the Herald API operator has deployed it. The API currently needs a configured upstream model backend before chat requests can generate answers. herald-core and herald-sentinel are public model aliases; they do not imply that Herald-trained model weights are already hosted.

## 1. What you'll need

- A public Herald API base URL from the project maintainer, for example https://your-herald-api.example (placeholder only).
- A Herald API key provided to you by the maintainer.
- Python 3.10+ or a recent Node.js release, depending on the example you choose.

Do not use the API operator's private server credentials or upstream provider key. Client projects should only receive their own Herald API key.

## 2. Set environment variables

Set these in your local shell, your hosting provider's secret/environment settings, or your deployment's secret manager. Do not commit real keys to GitHub.

Example shell session (replace the placeholder values):

~~~sh
export HERALD_API_BASE_URL="https://YOUR_PUBLIC_HERALD_API_HOST"
export HERALD_API_KEY="YOUR_HERALD_API_KEY"
~~~

Use the exact public HTTPS base URL shared by the maintainer. Do not add a trailing slash.

## 3. Python example

No third-party package is needed; this uses Python's standard library.

Save as herald_example.py:

~~~python
import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

BASE_URL = os.environ["HERALD_API_BASE_URL"].rstrip("/")
API_KEY = os.environ["HERALD_API_KEY"]


def ask_herald(message: str, model: str = "herald-core") -> str:
    if model not in {"herald-core", "herald-sentinel"}:
        raise ValueError("model must be 'herald-core' or 'herald-sentinel'")

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": message}],
        "stream": False,
    }
    request = Request(
        f"{BASE_URL}/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urlopen(request, timeout=90) as response:
            result = json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Herald API returned HTTP {exc.code}: {detail}") from exc
    except URLError as exc:
        raise RuntimeError(f"Could not reach the Herald API: {exc.reason}") from exc

    try:
        return result["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError("Herald returned an unexpected chat response.") from exc


if __name__ == "__main__":
    print(ask_herald("Hello, Herald!"))
~~~

Run it:

~~~sh
python herald_example.py
~~~

To use the more capable model alias, change the call to:

~~~python
ask_herald("Help me reason through this problem.", model="herald-sentinel")
~~~

## 4. JavaScript / Node.js example

This uses the built-in fetch API available in modern Node.js.

Save as herald-example.mjs:

~~~javascript
const baseUrl = process.env.HERALD_API_BASE_URL?.replace(/\/$/, "");
const apiKey = process.env.HERALD_API_KEY;

if (!baseUrl || !apiKey) {
  throw new Error("Set HERALD_API_BASE_URL and HERALD_API_KEY first.");
}

async function askHerald(message, model = "herald-core") {
  if (!["herald-core", "herald-sentinel"].includes(model)) {
    throw new Error("model must be 'herald-core' or 'herald-sentinel'");
  }

  const response = await fetch(baseUrl + "/v1/chat/completions", {
    method: "POST",
    headers: {
      Authorization: "Bearer " + apiKey,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      model,
      messages: [{ role: "user", content: message }],
      stream: false,
    }),
  });

  const result = await response.json().catch(() => ({}));

  if (!response.ok) {
    throw new Error(
      "Herald API returned HTTP " + response.status + ": " +
      (result?.error?.message ?? "Unknown API error")
    );
  }

  return result.choices?.[0]?.message?.content ?? "";
}

console.log(await askHerald("Hello from Node.js!"));
~~~

Run it:

~~~sh
node herald-example.mjs
~~~

## 5. Quick test with curl

~~~sh
curl "$HERALD_API_BASE_URL/v1/chat/completions" \
  -H "Authorization: Bearer $HERALD_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "herald-core",
    "messages": [{"role": "user", "content": "Hello, Herald!"}],
    "stream": false
  }'
~~~

A successful OpenAI-compatible response normally contains choices[0].message.content.

## 6. Available endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | /health | Public service health/configuration check |
| GET | /v1/models | List model aliases configured by the operator (API key required) |
| POST | /v1/chat/completions | Send a chat request (API key required) |

## 7. Common errors

- **401 — Authentication error:** check that the API key is correct and sent as Authorization: Bearer YOUR_KEY.
- **503 — Model not configured:** the API operator must configure the upstream URL and model mapping before this alias can answer.
- **502 — Upstream error:** the API could not get a valid response from the configured model provider; contact the operator.
- **404 / connection failure:** verify the base URL and that the API is deployed and reachable.

## Security tips

- Never publish your API key in source code, screenshots, public issues, or a public GitHub repository.
- Store keys in environment variables or your platform's secret manager.
- If your project is a public website or a client-side app, **do not embed a private key in browser/mobile code**. Put API calls behind your own server, where your key stays secret.
- Ask the project maintainer for your own key. Do not share one private test key across the public.
- The initial API version does not support streaming responses.
- The API maintainer may set quotas or revoke access; treat keys as credentials.

## About herald-link

These examples call the HTTP API directly so developers can integrate immediately without waiting for a client library. A dedicated herald-link SDK can later wrap the same API with a simpler interface, retries, and clearer error handling.
