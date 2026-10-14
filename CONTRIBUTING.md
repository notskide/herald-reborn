# Contributing to Herald Reborn

Thanks for helping build Herald Reborn. The project is in an early stage, so clear, sourced, small contributions are especially useful.

## Knowledge-entry guidelines

- Keep one entry focused on one topic.
- Prefer clear, direct language and define unfamiliar terms.
- Include source URLs for claims that can be checked externally.
- Summarize in original wording; do not copy source material at length.
- Separate established information from interpretation or open questions.
- Add related-entry IDs when they genuinely help readers navigate.
- Do not include private information, credentials, or copyrighted text copied at length.
- Update knowledge/index.json when adding or renaming entries.
- Leave entries as draft until a person has checked important claims and source relevance.

## Before submitting

Run:

    python scripts/validate_knowledge.py
    python scripts/search_knowledge.py --query "a representative question"

Then check for duplicate entries, verify source URLs, and explain what changed and why in the pull request. The validator checks structure and relationships; it cannot prove that every claim is true.
