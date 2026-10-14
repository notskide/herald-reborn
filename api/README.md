# herald-api (Wispbyte starter)

herald-api is the lightweight API gateway for Herald Reborn. It exposes Herald model IDs to client apps and forwards requests to a configured **OpenAI-compatible chat-completions backend**.

> **Important:** this is an API gateway, not a trained language model. It does not contain model weights. herald-core and herald-sentinel only answer requests after you map them to model IDs that actually exist on your configured backend. Using a temporary third-party model is a prototype, not a Herald-trained model.

## Deploy on Wispbyte

1. Create a Python server on [Wispbyte](https://wispbyte.com/client).
2. Upload the files in this api folder to the server's working/root directory: main.py and requirements.txt. Do not upload a real .env file or any secrets.
3. In Startup, set the startup command to:

        python -m pip install -r requirements.txt && python main.py

   If Wispbyte's selected Python image already installs requirements.txt for you, python main.py is enough. The app binds to 0.0.0.0 and uses PORT, then SERVER_PORT, with 8080 as a local fallback. Confirm the port variable/value in your server panel matches the public port allocated to your server.

4. In Startup / Environment Variables, add the values below. Keep secrets in the panel, not in GitHub.

   | Variable | Required | Purpose |
   |---|---|---|
   | HERALD_API_KEY | Yes | Private client key required by /v1/* routes |
   | HERALD_UPSTREAM_BASE_URL | Yes for chat | Base URL of the OpenAI-compatible backend, including /v1 if required |
   | HERALD_UPSTREAM_API_KEY | Depends on provider | Secret key for the upstream model service; can be blank for a backend that needs no key |
   | HERALD_CORE_UPSTREAM_MODEL | To enable core | Actual upstream model ID to route herald-core to |
   | HERALD_SENTINEL_UPSTREAM_MODEL | To enable sentinel | Actual upstream model ID to route herald-sentinel to |
   | HERALD_UPSTREAM_TIMEOUT_SECONDS | No | Timeout in seconds; defaults to 60 |

5. Start the server and check the console. Open https://YOUR_PUBLIC_HOST/health; it should return JSON. Add /docs to inspect the interactive API docs.

## Test it

/health is public and only reports whether configuration values are present. /v1/models and /v1/chat/completions require the private key:

    curl https://YOUR_PUBLIC_HOST/v1/models \
      -H "Authorization: Bearer YOUR_HERALD_API_KEY"

    curl https://YOUR_PUBLIC_HOST/v1/chat/completions \
      -H "Authorization: Bearer YOUR_HERALD_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "herald-core",
        "messages": [{"role": "user", "content": "Hello from Herald"}],
        "stream": false
      }'

The chat request will return a clear 503 until the base URL and the selected model mapping are configured. This prevents the API from pretending it has a model when it does not.

## Security and current limitations

- Never commit real API keys to GitHub or put them into public tutorials.
- The single HERALD_API_KEY is only a **private-test gate**. Do not distribute one shared key to the public. Before inviting community users, add per-user keys, revocation, usage limits/rate limiting, and abuse monitoring.
- Streaming is not supported in this initial version (stream must be false).
- The upstream URL must be an OpenAI-compatible base URL with a POST /chat/completions route.
- No chat content is logged by this app. Use HTTPS when exposing the server publicly.
- The free Wispbyte instance is suitable for a small API gateway prototype, not for hosting substantial model weights or heavy inference.
