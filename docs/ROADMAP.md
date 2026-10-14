# Herald Reborn roadmap

This roadmap is provisional and will change as the project is tested.

## Phase 1 — Knowledge foundation

- [x] Create repository overview and initial knowledge entries
- [x] Define entry conventions and a JSON index
- [x] Add automated checks for index paths, duplicate IDs, and related links
- [x] Expand the corpus across AI foundations, training, retrieval, applications, deployment, safety, and evaluation
- [ ] Review draft entries and promote only checked entries to reviewed
- [ ] Choose and add an explicit open-source license

## Phase 2 — Search and evidence quality

- [x] Implement lightweight keyword search
- [x] Add tag and status filters
- [x] Establish stable entry IDs, source metadata, and cross-links
- [ ] Create a small, versioned retrieval evaluation set
- [ ] Measure ranking and tune from observed failures
- [x] Add a small lexical alias/synonym map for common terms and abbreviations
- [ ] Explore semantic or hybrid retrieval only if it solves a measured problem

## Phase 3 — Assistant integration

- [x] Define a portable retrieval interface
- [x] Build a context builder that selects a bounded set of relevant entries
- [ ] Add a response planner for unsupported, ambiguous, and conflicting-evidence questions
- [ ] Connect retrieval to a configured model inference backend
- [ ] Return entry IDs or source URLs with grounded answers
- [ ] Keep external browsing separate from Dictionary facts
- [ ] Track source freshness and uncertainty

## Phase 4 — Quality, safety, and resource budgets

- [x] Add regression tests for empty retrieval, injected instructions in retrieved content, and source metadata
- [ ] Measure memory, latency, and quality under realistic request load
- [ ] Add red-team cases and a documented safety review checklist
- [ ] Review source permissions and provenance before marking content reviewed
- [ ] Publish reproducible evaluation reports for major search/runtime releases

## Phase 5 — Controlled growth

- [ ] Propose updates from approved sources
- [ ] Validate and review changes before merging
- [ ] Keep a transparent change history
- [ ] Monitor source freshness and retire stale claims
- [ ] Expand further only with a taxonomy, reliable sources, and test queries

## Guiding principle

A large corpus is useful only when it remains accurate, traceable, relevant, and searchable. More text is not automatically more intelligence: retrieval must find the right entry, sources must support claims, and the runtime must distinguish missing evidence from a definitive answer. Adding an entry does not itself train a model.
