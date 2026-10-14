# Herald Reborn

Herald Reborn is an evolving AI project with a structured knowledge layer and clear examples for connecting applications to the Herald API.

## What this repository contains

- `docs/` — public developer guides and integration examples
- `knowledge/` — curated knowledge entries and indexes
- `schemas/` — validation schemas for knowledge data

## Connect Herald to your project

Start with the [Connect a script to Herald guide](docs/connecting-to-herald.md). It includes copy-and-paste examples for Python, Node.js, and `curl`, plus request formats, authentication, and troubleshooting.

To make a request, a developer needs a Herald API base URL and an API key supplied by the API operator. This repository focuses on the client-side code developers use to connect their projects; it does not prescribe where the API must run.

## Model names

Examples use the public model aliases `herald-core` and `herald-sentinel`. The aliases identify the model options exposed by the API; they do not, by themselves, mean that trained model weights are included in this repository.

## Principles

- **Structured:** use consistent formats and metadata.
- **Connected:** link related concepts explicitly.
- **Traceable:** record sources and distinguish established facts from hypotheses.
- **Incremental:** make small, reviewable improvements.
- **Resource-conscious:** keep the knowledge layer usable on modest hardware.

## Status

Early foundation stage. The repository and its conventions will evolve as Herald develops.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.
