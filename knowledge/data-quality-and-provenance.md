---
id: data-quality-and-provenance
title: "Data Quality and Provenance"
summary: "How dataset quality, source tracking, duplication, leakage, and coverage affect trustworthy AI systems."
tags: ["data", "quality", "provenance", "evaluation"]
related: ["knowledge-repositories", "learning-and-memory", "evaluation-and-test-sets", "uncertainty-and-conflicting-evidence"]
sources: ["https://scikit-learn.org/stable/common_pitfalls.html", "https://www.nist.gov/itl/ai-risk-management-framework"]
status: draft
updated: 2026-10-14
---

# Data Quality and Provenance

Data quality describes whether information is suitable for its intended use. Provenance records where information came from, how it was transformed, and when it was collected or reviewed.

## Useful checks

- **Accuracy:** does the data represent the intended fact or event?
- **Coverage:** are important topics, languages, user groups, or edge cases missing?
- **Consistency:** do records use compatible units, labels, identifiers, and formats?
- **Freshness:** could a once-correct statement have become outdated?
- **Duplication:** are repeated records over-representing a narrow set of examples?
- **Label quality:** are annotations clear and consistent?
- **Data leakage:** has information from an evaluation set improperly entered training or model selection, making results look better than real-world performance?

## Provenance for a knowledge dictionary

Each entry should have a stable ID, source URLs, update date, review status, and links to related concepts. If credible sources disagree, record the disagreement rather than silently choosing one. A source URL is a place to investigate a claim, not proof that the claim is correct or current.

## Practical workflow

Define the intended use; collect permitted sources; remove accidental duplicates; identify sensitive information; record transformations and dates; sample records for errors; validate the schema; and keep changes reviewable. Re-check high-impact or time-sensitive content periodically.

## Sources

- https://scikit-learn.org/stable/common_pitfalls.html
- https://www.nist.gov/itl/ai-risk-management-framework
