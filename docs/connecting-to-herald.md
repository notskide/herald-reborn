# connect to Herald

so you want to use Herald in your own project? this is the guide.

the Herald API is ready at:

**https://herald.wisp.uno**

the API interface and routes are ready to be used. the AI model itself hasn't been implemented into the API yet, so chat requests won't generate actual Herald responses for now. that part is still being worked on.

## 1. what you'll need

- the Herald API URL: `https://herald.wisp.uno`
- a Herald API key, if authentication is enabled for your access
- Python 3.10+ or a recent Node.js release, depending on the example you choose

don't put private server credentials or upstream provider keys in your project. keep your own API key private too.

## 2. set the API URL

you can use the public URL directly:

~~~sh
export HERALD_API_BASE_URL="https://herald.wisp.uno"
export HERALD_API_KEY="YOUR_HERALD_API_KEY"
~~~

don't add a trailing slash to the base URL. keep your API key in an environment variable and never commit a real key to GitHub.

## 3. Python example

this uses Python's standard library, so no extra packages are needed.

save as `herald_example.py`:

~~~python
import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

BASE_URL = os.environ.get("HERALD_API_BASE_URL", "https://herald.wisp.uno").rstrip("/")
API_KEY = os.environ["HERALD_API_KEY"]


def ask_herald(message: str, model: str = "herald-core") -> str:
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

run it with:

~~~sh
python herald_example.py
~~~

**heads up:** the API is ready, but the AI model hasn't been connected yet. this example shows how your project will send a request once model integration is finished. it isn't expected to return an AI generated answer yet.

## 4. JavaScript / Node.js example

this uses the built in `fetch` API available in modern Node.js.

save as `herald-example.mjs`:

~~~javascript
const baseUrl = (process.env.HERALD_API_BASE_URL || "https://herald.wisp.uno").replace(/\\/$/, "");
const apiKey = process.env.HERALD_API_KEY;

if (!apiKey) {
  throw new Error("Set HERALD_API_KEY first.");
}

async function askHerald(message, model = "herald-core") {
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

run it with:

~~~sh
node herald-example.mjs
~~~

the example is ready for when the model is connected. until then, chat requests won't produce a generated response.

## 5. quick test with curl

~~~sh
curl "https://herald.wisp.uno/v1/chat/completions" \
  -H "Authorization: Bearer $HERALD_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "herald-core",
    "messages": [{"role": "user", "content": "Hello, Herald!"}],
    "stream": false
  }'
~~~

the API uses an OpenAI compatible chat request format. actual chat responses depend on the AI model being connected.

## 6. available endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | /health | Check the API service |
| GET | /v1/models | List model aliases exposed by the API |
| POST | /v1/chat/completions | Send a chat request |

the routes are part of the API interface. model backed chat generation is not available until the AI model is implemented and connected.

## 7. common errors

- **401: authentication error.** check that your API key is correct and sent as `Authorization: Bearer YOUR_KEY`.
- **503: model not configured.** the API is reachable, but the AI model hasn't been connected yet.
- **502: upstream error.** the API couldn't get a valid response from its configured backend.
- **404 or connection failure.** check the URL and whether the service is reachable.

## security tips

- never publish your API key in source code, screenshots, public issues, or a public GitHub repository.
- store keys in environment variables or your platform's secret manager.
- if your project is a public website or a client side app, don't put a private key in browser or mobile code. put API calls behind your own server.
- don't share private test keys publicly.
- the initial API version does not support streaming responses.

## about herald-link

these examples call the HTTP API directly, so developers can start integrating without waiting for a client library. a dedicated `herald-link` SDK could wrap the same API later with a simpler interface, retries, and clearer errors.
