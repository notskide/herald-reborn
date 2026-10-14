---
id: knowledge-graphs-and-ontologies
title: "Knowledge Graphs and Ontologies"
summary: "Representing entities and their relationships explicitly to support traversal, consistency, and explainable retrieval."
tags: ["knowledge-graphs","ontology","retrieval","data-modeling"]
related: ["knowledge-repositories","retrieval-augmented-generation","data-quality-and-provenance"]
sources: ["https://www.w3.org/TR/prov-overview/","https://www.w3.org/TR/rdf11-concepts/"]
status: draft
updated: 2026-10-14
---

# Knowledge Graphs and Ontologies

A knowledge graph represents entities and relations as connected records. An ontology describes entity types, relationships, and sometimes constraints on their meaning. A graph might express dependencies between software packages, parent-child relationships between concepts, or which source supports a claim.

Graphs support queries that follow relationships rather than simply matching words. They can connect aliases, group topics, and help explain why a result was found. A graph can complement document retrieval: edges identify related concepts while source documents preserve detailed evidence.

Use stable identifiers, canonical names, aliases, and disambiguation rules. Record provenance for each fact, including source, date, and verification status. Distinguish directly asserted facts from inferred relationships. A missing edge does not prove that a relationship is false.

Graph construction can be expensive and error-prone. The same name may refer to different entities, and different sources may use different names for one concept. Ontology constraints can also become brittle as a domain changes.

For Herald, stable entry IDs and related-entry links already form a small explicit graph. Expand incrementally with aliases, concept types, and source-level provenance before adding a separate graph database.

## Sources

- https://www.w3.org/TR/prov-overview/
- https://www.w3.org/TR/rdf11-concepts/

## Sources

- https://www.w3.org/TR/prov-overview/
- https://www.w3.org/TR/rdf11-concepts/
