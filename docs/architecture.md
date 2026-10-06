# Architecture

## v0.1 public architecture

```text
Sources
  ↓
Collectors / adapters
  ↓
Evidence
  ↓
Normalization
  ↓
Entities
  ↓
Graph
  ↓
Datasets
  ↓
Analysis / API
```

The architecture separates raw observations from derived analysis.

### Evidence

An evidence item represents an externally observable fact together with provenance. The storage boundary should preserve the distinction between an observation and a derived interpretation.

### Entities

Entities are generic representations of addresses, transactions, contracts, tokens, agents, or other identifiable objects. Private ASPYP entity-resolution mappings are excluded.

### Graph

The graph layer represents relationships between entities and evidence and supports deterministic construction and traversal without assuming a proprietary risk model.

### Datasets

Datasets are analysis-ready projections of evidence and graph state. Schemas should be explicit and versionable.

### Analysis

The public layer exposes generic analysis primitives and extension points. Commercial risk scoring and private inference logic remain outside this repository.

## Design constraint

The engine must be usable with independently sourced data and must not require a private ASPYP service, private dataset, or secret credential.
