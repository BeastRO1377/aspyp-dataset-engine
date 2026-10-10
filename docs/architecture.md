# Architecture

## Intended public architecture

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

The first public schema is `evm-transfer/v1`. It accepts a provider-adapted transfer observation,
validates its structural invariants, and serializes raw units as decimal strings. Provider clients,
credentials, storage, and any attribution or risk decisions remain outside this boundary.

### Analysis

The public layer exposes generic analysis primitives and extension points. Commercial risk scoring and private inference logic remain outside this repository.

## Design constraint

The engine must be usable with independently sourced data and must not require a private ASPYP service, private dataset, or secret credential.

## Implemented in v0.2.0

Only EVM transfer normalization and serialization are implemented. Other package namespaces are placeholders. The public package does not collect or store mainnet observations or address labels. See the mainnet investigation roadmap for the proposed next phase.
