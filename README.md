# Herald Reborn

A growing, structured knowledge base designed as the foundation for an evolving, resource-conscious AI assistant.

## Vision

Herald Reborn aims to organize knowledge into connected, searchable entries that can expand over time and eventually support an assistant that can retrieve information, reason across concepts, and use live internet sources when available.

This repository does not claim that the system is conscious or that a complete AI assistant already exists.

## Project structure

- `api/` — the initial `herald-api` gateway prototype and Wispbyte deployment guide
- `knowledge/` — curated knowledge entries and indexes
- `schemas/` — validation schemas for knowledge data
- `docs/` — design notes and roadmap

## Herald API prototype

The first API gateway version exposes the public model IDs `herald-core` and `herald-sentinel` and forwards chat requests to an explicitly configured OpenAI-compatible backend.

The gateway is not itself a trained model and does not include model weights. It needs real upstream model IDs and backend configuration before chat requests can succeed. The single API key in this prototype is for private testing only; per-user keys, quotas, and rate limiting are needed before a public launch.

See the [API deployment guide](api/README.md) for Wispbyte setup instructions.

## Principles

- **Structured:** use consistent formats and metadata.
- **Connected:** link related concepts explicitly.
- **Traceable:** record sources and distinguish established facts from hypotheses.
- **Incremental:** make small, reviewable improvements.
- **Resource-conscious:** keep the knowledge layer usable on modest hardware.

## Status

Early foundation stage. The repository now includes an initial API gateway prototype alongside the knowledge base. The structure and conventions will evolve as the project develops.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

## Use Herald in your project

Developers can follow the [Connect a script to Herald guide](docs/connecting-to-herald.md) for copy-and-paste Python, Node.js, and curl examples. You do not need to host the API yourself; use the public API URL and an API key provided by the project maintainer once the service is deployed.

API operators setting up the server should use the [Wispbyte deployment guide](api/README.md).
