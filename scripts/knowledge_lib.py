"""Dependency-free loading and lexical retrieval for the Herald dictionary."""
from __future__ import annotations
import json
import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

TOKEN_RE = re.compile(r"[\w]+", re.UNICODE)
REQUIRED_FIELDS = {"id", "title", "summary", "tags", "related", "sources", "status", "updated"}

@dataclass(frozen=True)
class KnowledgeEntry:
    id: str
    title: str
    summary: str
    tags: tuple[str, ...]
    related: tuple[str, ...]
    sources: tuple[str, ...]
    status: str
    updated: str
    path: str
    body: str

def tokenize(text: str) -> list[str]:
    return [token for token in TOKEN_RE.findall(text.casefold()) if len(token) > 1]

def _parse_value(value: str):
    value = value.strip()
    if value.startswith("[") or value.startswith('"'):
        return json.loads(value)
    return value

def parse_front_matter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing opening front-matter delimiter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("missing closing front-matter delimiter")
    metadata = {}
    for line_number, line in enumerate(text[4:end].splitlines(), start=2):
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"invalid front-matter line {line_number}")
        key, value = line.split(":", 1)
        key = key.strip()
        if not key or key in metadata:
            raise ValueError(f"empty or duplicate metadata field on line {line_number}")
        metadata[key] = _parse_value(value)
    return metadata, text[end + 5:].strip()

def parse_entry_file(path: Path) -> KnowledgeEntry:
    meta, body = parse_front_matter(path.read_text(encoding="utf-8"))
    missing = REQUIRED_FIELDS - set(meta)
    if missing:
        raise ValueError(f"{path}: missing fields: {', '.join(sorted(missing))}")
    for field in ("tags", "related", "sources"):
        if not isinstance(meta[field], list) or any(not isinstance(v, str) for v in meta[field]):
            raise ValueError(f"{path}: {field} must be an array of strings")
    body = re.split(r"\n## Sources\s*\n", body, maxsplit=1)[0].strip()
    return KnowledgeEntry(
        id=str(meta["id"]), title=str(meta["title"]), summary=str(meta["summary"]),
        tags=tuple(meta["tags"]), related=tuple(meta["related"]), sources=tuple(meta["sources"]),
        status=str(meta["status"]), updated=str(meta["updated"]), path=path.name, body=body,
    )

def load_entries(knowledge_dir: Path) -> list[KnowledgeEntry]:
    index = json.loads((knowledge_dir / "index.json").read_text(encoding="utf-8"))
    entries = []
    for record in index.get("entries", []):
        relative = Path(record["path"])
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError(f"unsafe index path: {record['path']}")
        path = (knowledge_dir / relative).resolve()
        if not path.is_relative_to(knowledge_dir.resolve()) or not path.is_file():
            raise ValueError(f"invalid or missing index path: {record['path']}")
        entry = parse_entry_file(path)
        if entry.id != record.get("id"):
            raise ValueError(f"index ID mismatch for {record['path']}")
        entries.append(entry)
    return entries

def search_entries(
    entries: Iterable[KnowledgeEntry], query: str, limit: int = 5,
    tag: str | None = None, status: str | None = None,
) -> list[tuple[KnowledgeEntry, float]]:
    if limit < 1:
        raise ValueError("limit must be at least 1")
    query_tokens = tokenize(query)
    if not query_tokens:
        return []

    # Small, transparent concept aliases improve matching without requiring
    # embeddings or an external service. Original query terms keep full weight;
    # expansion terms are deliberately weaker to avoid overpowering exact hits.
    query_weights = {term: 1.0 for term in query_tokens}
    normalized_query = " ".join(query_tokens)
    aliases = {
        "llm": ("large language model",),
        "large language model": ("llm",),
        "rag": ("retrieval augmented generation",),
        "retrieval augmented generation": ("rag",),
        "gen ai": ("generative artificial intelligence",),
        "generative ai": ("generative artificial intelligence",),
        "speech to text": ("speech recognition", "automatic speech recognition", "transcription", "asr"),
        "text to speech": ("speech synthesis", "spoken audio", "tts"),
        "voice recognition": ("speech recognition", "asr"),
        "ocr": ("optical character recognition", "document parsing"),
        "vector db": ("vector database", "vector search", "embeddings"),
        "vector database": ("vector db", "vector search", "embeddings"),
        "fine tuning": ("fine-tuning", "finetuning"),
        "prompt hacking": ("prompt injection", "untrusted content"),
        "ai agent": ("agent tool use", "planning", "function calling"),
        "ai agents": ("agent tool use", "planning", "function calling"),
        "hallucination": ("hallucinations", "grounding", "unsupported answer"),
        "memory usage": ("memory", "ram", "low-resource inference"),
        "reduce ram": ("memory", "quantization", "low-resource inference"),
    }
    for phrase, expansions in aliases.items():
        if phrase in normalized_query:
            for expansion in expansions:
                for term in tokenize(expansion):
                    query_weights[term] = max(query_weights.get(term, 0.0), 0.45)
    # Normalize common singular/plural variants as low-weight alternatives.
    for term in list(query_weights):
        if len(term) > 4 and term.endswith("ies"):
            query_weights.setdefault(term[:-3] + "y", 0.35)
        elif len(term) > 4 and term.endswith("s") and not term.endswith("ss"):
            query_weights.setdefault(term[:-1], 0.35)
    all_entries = list(entries)
    candidates = [
        e for e in all_entries
        if (tag is None or tag.casefold() in {t.casefold() for t in e.tags})
        and (status is None or status == e.status)
    ]
    if not candidates:
        return []
    docs = [tokenize(f"{e.title} {e.summary} {e.body}") for e in candidates]
    count = len(docs)
    lengths = [len(doc) for doc in docs]
    average_length = (sum(lengths) / count) if count else 1.0
    df = {}
    for doc in docs:
        for term in set(doc):
            df[term] = df.get(term, 0) + 1
    terms_in_query = query_weights
    phrase = " ".join(query_tokens)
    scored = []
    for entry, terms, length in zip(candidates, docs, lengths):
        tf = {}
        for term in terms:
            tf[term] = tf.get(term, 0) + 1
        title_terms = set(tokenize(entry.title))
        summary_terms = set(tokenize(entry.summary))
        tag_terms = {t.casefold() for t in entry.tags}
        score = 0.0
        for term, weight in terms_in_query.items():
            if term not in df:
                continue
            idf = math.log(1 + (count - df[term] + 0.5) / (df[term] + 0.5))
            frequency = tf.get(term, 0)
            if frequency:
                k1, b = 1.5, 0.75
                denom = frequency + k1 * (1 - b + b * length / max(average_length, 1.0))
                score += weight * idf * (frequency * (k1 + 1)) / denom
            if term in title_terms:
                score += weight * 1.8 * idf
            if term in summary_terms:
                score += weight * 0.8 * idf
            if term in tag_terms:
                score += weight * 1.2 * idf
        title_phrase = " ".join(tokenize(entry.title))
        body_phrase = " ".join(tokenize(entry.body))
        if phrase and (phrase in title_phrase or phrase in body_phrase):
            score += 1.0
        if score > 0:
            scored.append((entry, score))
    scored.sort(key=lambda item: (-item[1], item[0].title.casefold()))
    return scored[:limit]
