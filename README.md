# Herald Reborn

**Herald is an independently developed AI assistant project built around Herald Core, a custom fine-tuned Qwen 2.5 1.5B model, and a source-linked knowledge system.**

The goal is to develop an independently operated assistant with its own model, retrieval layer, tools, and eventually a reliable public inference API.

> **Development status:** Herald Core's 1.5B checkpoint has been tested through the project's local inference workflow. This repository currently publishes the knowledge corpus, retrieval/context-building utilities, schemas, and developer documentation. The model checkpoint, full training artifacts, and a continuously hosted public inference service are not included here.

## Project components

- **Herald Core:** the language-model component. The current 1.5B checkpoint is based on Qwen 2.5 1.5B Instruct and has been tested locally. Model weights are not stored in this repository.
- **Herald's Dictionary:** a structured, source-linked knowledge collection covering AI concepts, model architecture, training, prompting, retrieval, inference, agents, tools, evaluation, privacy, safety, and governance.
- **Retrieval tools:** lightweight search and bounded context-building utilities that select relevant knowledge entries for a model.
- **Developer integration:** documentation and examples describing the planned OpenAI-compatible Herald API interface.

## Repository contents

- `knowledge/`: the growing Dictionary of AI concepts and implementation practices.
- `scripts/`: dependency-free validation, keyword search, and context-building tools.
- `schemas/`: metadata schema for knowledge entries.
- `docs/`: developer integration guide and project roadmap.
- `.github/workflows/`: automated checks for Dictionary consistency and search behavior.

## Herald's Dictionary

The Dictionary currently contains **82 indexed topics**. Each entry is a focused Markdown document with a stable ID, summary, tags, related entries, source links, review status, and update date.

The corpus is a growing reference collection, not a complete encyclopedia. New and expanded material starts as `draft` until its sources and important claims have been deliberately reviewed. Retrieved text is reference material, not executable instructions, and an entry does not train the model simply because it exists.

## Use the knowledge tools

Run these commands from the repository root:

```bash
python scripts/validate_knowledge.py
python scripts/search_knowledge.py --query "How does retrieval-augmented generation work?"
python scripts/search_knowledge.py --query "quantization memory" --limit 5
python scripts/search_knowledge.py --query "privacy" --tag security
```

### Build bounded context for a model

The context builder selects relevant Dictionary entries, includes their IDs and source URLs, flags draft-only evidence, and enforces a character budget.

```bash
python scripts/context_builder.py --query "How does retrieval-augmented generation work?" --limit 4 --max-chars 6000
python -m unittest discover -s scripts -p "test_*.py" -v
```

This prepares evidence for a model; it does not generate an answer by itself. A model inference runtime is still required for chat generation.

## Model and inference status

The current Herald Core model is based on **Qwen 2.5 1.5B Instruct**. Its checkpoint has been tested through the local Herald inference workflow.

A few important distinctions:

- The checkpoint is not committed to this repository.
- The Dictionary and context builder support the broader assistant project; they are not the language model itself.
- The public API examples document an integration target. They do not mean a public Herald endpoint is currently deployed.
- The model aliases `herald-core` and `herald-sentinel` are API-facing names used in examples, not proof that two separate hosted models are available.

See [the project roadmap](docs/ROADMAP.md) for planned work and [the API integration guide](docs/connecting-to-herald.md) for the current prototype interface.

## Project principles

- **Independent:** build and operate Herald as its own AI project.
- **Traceable:** keep knowledge entries connected to sources and distinguish evidence from inference.
- **Grounded:** retrieve relevant context and preserve source metadata.
- **Incremental:** make small, testable improvements.
- **Resource-conscious:** keep retrieval portable and mindful of limited compute.
- **Honest:** document what works, what is experimental, and what is not deployed. Never invent model weights, sources, benchmarks, or capabilities.

## Current focus

Herald is under active development. Current work centers on improving the model and its inference workflow, strengthening the knowledge/retrieval layer, and finding sustainable compute for persistent hosting.

The long-term goal is a continuously available Herald service with a reliable API, while keeping the model, knowledge system, and deployment status clearly documented.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.
