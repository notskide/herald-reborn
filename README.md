# herald reborn

yoo, welcome to Herald.

Herald is an AI assistant project i'm building. the goal is to give it its own language model, a knowledge base it can search through, and eventually an API that people can actually use.

> **where we're at:** the current model checkpoint has been tested with the local inference setup. this repo has the knowledge collection, search and context building scripts, schemas, and docs. the model files aren't here, and there isn't a public 24/7 endpoint yet.

## what's in here?

- **Herald Core**: the language model behind the project. the current checkpoint has been tested locally, but the weights aren't in this repo.
- **Herald's Dictionary**: notes and references about AI, models, training, retrieval, tools, safety, and other related topics.
- **search and context tools**: scripts that find useful entries and prepare relevant information for the model.
- **developer docs**: notes about the API prototype and what still needs to happen.

## repo map

- `knowledge/` contains the Dictionary and its index
- `scripts/` contains validation, search, and context building scripts
- `schemas/` contains the format used for Dictionary entries
- `docs/` contains the roadmap and API notes
- `.github/workflows/` contains automated checks

## the Dictionary

there are **82 indexed topics** in the Dictionary right now. each topic has its own Markdown file with an ID, summary, tags, related topics, sources, and a review status.

it's a growing collection of references, not some all knowing encyclopedia. new entries start as `draft` until their sources and important claims have been checked.

also, adding something to the Dictionary does not magically train the model. it just gives the retrieval tools something useful to find and pass to it.

## try the tools

run these from the repo's root folder:

```bash
python scripts/validate_knowledge.py
python scripts/search_knowledge.py --query "How does retrieval-augmented generation work?"
python scripts/search_knowledge.py --query "quantization memory" --limit 5
python scripts/search_knowledge.py --query "privacy" --tag security
```

### preparing context for the model

the context builder looks for relevant Dictionary entries, keeps their IDs and source links, flags draft material, and stays within a character limit.

```bash
python scripts/context_builder.py --query "How does retrieval-augmented generation work?" --limit 4 --max-chars 6000
python -m unittest discover -s scripts -p "test_*.py" -v
```

these scripts prepare information for a model. they don't generate a chat response by themselves, so an inference runtime is still needed.

## model and hosting situation

the current Herald Core checkpoint has been tested locally. i'm not publishing the underlying model details here.

a few things worth knowing:

- the model checkpoint isn't stored in this repository.
- the Dictionary and retrieval scripts support Herald, but they aren't the model itself.
- the API guide describes the interface we're working towards. there isn't a public Herald API running yet.
- `herald-core` and `herald-sentinel` are example API names. they don't mean two separate hosted models are available.

the [roadmap](docs/ROADMAP.md) has the planned work. the [API guide](docs/connecting-to-herald.md) explains the current prototype interface.

## a few things i care about

- **sources matter.** knowledge entries should link to where the information came from.
- **don't make stuff up.** confirmed facts, guesses, and examples should be kept separate.
- **keep it manageable.** small changes that can be tested are better than huge mystery updates.
- **be realistic about compute.** Herald needs to work with the resources we can actually get.
- **be honest about progress.** if something is experimental or not online yet, just say that.

## what's next?

there's still a lot to do. i'm working on the model and inference setup, improving the knowledge tools, and trying to find compute that can keep Herald online 24/7.

that's the goal. we're not there yet, but i'm still working on it.

if you're interested, feel free to look around the repo, open an issue, or share some feedback. help is welcome.

## contributing

if you want to help out, check [CONTRIBUTING.md](CONTRIBUTING.md).
