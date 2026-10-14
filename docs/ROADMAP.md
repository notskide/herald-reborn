# Herald Reborn roadmap

This roadmap is provisional and will change as the project is tested.

## Phase 1 — Knowledge foundation

- [x] Create repository overview and initial knowledge entries
- [x] Define entry conventions and a JSON index
- [x] Add automated checks for index paths, duplicate IDs, and broken related links
- [x] Expand the initial corpus across core AI, retrieval, evaluation, and safety topics
- [ ] Review draft entries and promote only checked entries to reviewed
- [ ] Choose and add an explicit open-source license

## Phase 2 — Search

- [x] Implement lightweight keyword search
- [x] Add tag and status filters
- [ ] Create a small, versioned retrieval evaluation set
- [ ] Measure query results and tune scoring from observed failures
- [ ] Explore semantic or hybrid retrieval only if it solves a measured problem

## Phase 3 — Assistant integration

- [x] Define stable entry IDs, source metadata, and a portable retrieval interface
- [ ] Connect retrieval to a configured model inference backend
- [ ] Return knowledge entry IDs or source URLs with grounded answers
- [ ] Keep external browsing separate from dictionary facts
- [ ] Track source freshness and uncertainty

## Phase 4 — Controlled growth

- [ ] Propose candidate updates from approved sources
- [ ] Validate and review changes before merging
- [ ] Keep a transparent change history
- [ ] Evaluate quality, latency, and memory use as the corpus grows

## Guiding principle

Build observable, testable pieces first. A growing repository is useful when updates remain accurate, traceable, and easy to maintain. Adding an entry does not itself train a model.
