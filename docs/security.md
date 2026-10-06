# Security

Security is a first-class design constraint because the engine processes externally sourced blockchain data and may be embedded in systems that make consequential decisions.

## Trust boundaries

1. external data sources;
2. ingestion and parsing;
3. evidence storage;
4. derived graph and dataset state;
5. downstream analysis or applications.

Untrusted source data must not be treated as trusted application configuration.

## Provenance and integrity

Evidence records should preserve source and acquisition metadata. Where applicable, implementations should support integrity checks and deterministic identifiers.

## Secrets

The public repository must never contain private keys, API credentials, access tokens, passwords, private endpoints, production configuration, or private ASPYP datasets.

## Data handling

Examples and tests must use synthetic or publicly redistributable data.
