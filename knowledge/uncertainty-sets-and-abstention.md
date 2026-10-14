---
id: uncertainty-sets-and-abstention
title: "Uncertainty Handling and Abstention"
summary: "When an assistant should acknowledge missing evidence, ask a question, or decline to give an unsupported answer."
tags: ["uncertainty","abstention","reliability","rag"]
related: ["uncertainty-and-conflicting-evidence","hallucinations-and-grounding","calibration-and-confidence"]
sources: ["https://www.nist.gov/itl/ai-risk-management-framework","https://scikit-learn.org/stable/modules/calibration.html"]
status: draft
updated: 2026-10-14
---

# Uncertainty Handling and Abstention

Abstention means intentionally not providing a definitive answer when evidence or capability is insufficient. A useful assistant can still explain what is known, identify missing information, or ask a targeted question.

The corpus may lack the answer, retrieval may return irrelevant passages, sources may conflict, the model may not support the requested modality, or the question may be ambiguous. In each case, a confident guess may be worse than an honest limitation.

Design a decision rule from measurable signals: retrieval relevance, source quality, source agreement, output validation, task-specific evaluation, and known capability boundaries. Tune thresholds on representative data and account for the cost of wrong answers versus unanswered questions. Do not treat assertive wording or raw token probabilities as calibrated truth scores.

Choose fallbacks that match the problem: ask for clarification when intent is ambiguous; state that evidence is missing when retrieval fails; provide a supported partial answer when possible; escalate high-impact cases; return a service error when infrastructure failed.

Track harmful overconfidence and unnecessary refusals. An assistant that abstains on every query is not useful. For Herald, “the Dictionary has no relevant entry” is not the same as “the question has no answer.”

## Sources

- https://www.nist.gov/itl/ai-risk-management-framework
- https://scikit-learn.org/stable/modules/calibration.html

## Sources

- https://www.nist.gov/itl/ai-risk-management-framework
- https://scikit-learn.org/stable/modules/calibration.html
