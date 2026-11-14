# herald reborn

hey, this is herald — an AI assistant project i'm building.

the idea is pretty simple: build an assistant with its own language model, a knowledge base it can look things up in, and eventually a public API that people can actually use.

> **where things are right now:** the current model checkpoint has been tested with the local inference setup. this repo contains the knowledge collection, search and context-building scripts, schemas, and docs. it does **not** contain the model files or a public 24/7 endpoint yet.

## what's in here?

- **herald core** — the language-model part of the project. the current checkpoint has been tested locally; the weights aren't in this repo.
- **herald's dictionary** — a collection of notes and references about AI, models, training, retrieval, tools, safety, and related topics.
- **search + context tools** — scripts that find useful entries and prepare a smaller chunk of context for the model.
- **developer docs** — notes on the planned API and where the project is heading.

## repo map

- `knowledge/` — the Dictionary and its index
- `scripts/` — validation, search, and context-building scripts
- `schemas/` — the format used for Dictionary entries
- `docs/` — roadmap and API integration notes
- `.github/workflows/` — automated checks

## the Dictionary

there are **82 indexed topics** in the Dictionary right now. each topic has its own Markdown file, with an ID, summary, tags, related topics, sources, and a review status.

it's a growing reference collection, not some all-knowing encyclopedia. new entries start as `draft` until their sources and important claims have been checked. also, adding something to the Dictionary doesn't magically train the model — it gives the retrieval tools something useful to find.

## try the tools

run these from the repo's root folder:

```bash
python scripts/validate_knowledge.py
python scripts/search_knowledge.py --query "How does retrieval-augmented generation work?"
python scripts/search_knowledge.py --query "quantization memory" --limit 5
python scripts/search_knowledge.py --query "privacy" --tag security
```

### preparing context for the model

the context builder finds relevant Dictionary entries, keeps their IDs and source links, flags draft material, and stays within a character limit.

```bash
python scripts/context_builder.py --query "How does retrieval-augmented generation work?" --limit 4 --max-chars 6000
python -m unittest discover -s scripts -p "test_*.py" -v
```

these scripts prepare information for a model to use. they don't generate a chat response on their own — you'll still need an inference runtime for that.

## model + hosting situation

the current Herald Core checkpoint has been tested locally. the details of the underlying model aren't published here.

a few things worth making clear:

- the model checkpoint isn't stored in this repository.
- the Dictionary and retrieval scripts are supporting parts of Herald, not the model itself.
- the API guide describes the interface we're working towards. there isn't a public Herald API running yet.
- `herald-core` and `herald-sentinel` are example API names; they don't mean two separate hosted models are available.

the [roadmap](docs/ROADMAP.md) has the planned work. the [API guide](docs/connecting-to-herald.md) explains the current prototype interface.

## a few things i care about

- **sources matter.** knowledge entries should point to where the information came from.
- **don't make stuff up.** keep facts, guesses, and examples separate.
- **keep it manageable.** small changes that can be tested are better than giant mystery updates.
- **be realistic about compute.** the project should work within the resources actually available.
- **be honest about progress.** if something is experimental or not deployed, say so.

## what's next?

right now, the work is around improving the model and inference setup, making the knowledge tools better, and finding compute that can keep Herald online 24/7.

that's the goal. we're not there yet, but the project is still moving.

if you want to follow along, check the repo and its issues. contributions and useful feedback are welcome.

## contributing

see [CONTRIBUTING.md](CONTRIBUTING.md) if you'd like to help.
