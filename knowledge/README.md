# herald's knowledge dictionary

this folder is basically Herald's reference shelf.

there are **82 indexed topics** here right now. they cover AI basics, model training, retrieval and RAG, inference, agents, multimodal systems, evaluation, security, and responsible deployment.

quick note: a folder full of knowledge files isn't a trained AI model. these entries give the retrieval system information it can find and pass to a model. the model is still what generates the actual response.

entries marked `draft` still need their sources and important claims checked.

## what does an entry look like?

each topic is a Markdown file with a small metadata block at the top. here's the general format:

    ---
    id: example-topic
    title: "Example topic"
    summary: "A one-sentence summary."
    tags: ["example", "foundations"]
    related: ["another-topic"]
    sources: ["https://example.com/source"]
    status: draft
    updated: 2026-10-14
    ---

the ID should be lowercase, use hyphens, and match the filename without `.md`. the allowed statuses are `draft`, `reviewed`, and `needs-update`.

use empty arrays if there aren't any known tags, links, or sources. please don't make up source URLs. primary research, official docs, standards, and reliable technical references are usually good places to start.

## adding or editing topics

a few things to keep this folder useful:

- keep each file focused on one topic.
- explain terms before relying on them.
- write explanations in your own words instead of copying huge chunks from a source.
- make it clear what's a confirmed fact, what's an example, and what's a recommendation.
- use the IDs of related entries, not their filenames or display titles.
- new or heavily changed entries should start as `draft`.
- only mark something `reviewed` after checking the important claims and sources.
- update the date when you actually check or change an entry.
- be extra careful with things that change quickly, like model details, security advice, and laws.
- don't add passwords, private chats, personal records, or copyrighted source dumps here.

## the index and scripts

`index.json` keeps track of the entries so the scripts can find them. if you add or rename a topic, its title, tags, related links, and file path need to match what's in the Markdown file.

the validator checks the metadata, duplicate IDs, source URL format, indexed files, and related topic links.

from the repo root, run:

    python scripts/validate_knowledge.py
    python scripts/search_knowledge.py --query "How does retrieval-augmented generation work?"
    python scripts/search_knowledge.py --query "quantization memory" --limit 5
    python scripts/search_knowledge.py --query "privacy" --tag security

no extra Python packages needed. the scripts use the standard library.
