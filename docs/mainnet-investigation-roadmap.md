# Mainnet investigation roadmap

This is a proposed next phase, not v0.2.0 functionality.

## 1. Establish source rights and isolate collection

Define whether the investigation data stays internal, is shared in reports, or becomes a downloadable dataset. For Etherscan obtain written scope for ASPYP's organisational use, metadata, retention and export rights. Where those rights are unsuitable, source onchain evidence independently from an appropriately licensed RPC/archive source and use independently redistributable labels. API availability does not establish data rights.

Keep the collector read-only, with no wallet signer, private keys, raw-transaction broadcast or payment/recovery calls. Payment tests remain testnet work; mainnet observation does not authorize mainnet fund movements. Implement provider adapters separately from the deterministic core.

## 2. Define evidence before ingestion

Key transfers by chain, transaction, execution origin and actual log/trace identity. Preserve block hash, acquisition time, source endpoint without credentials, schema version, raw-payload digest, execution status and finality. Do not generate fake log indices from page order or `transactionIndex`. Track incomplete observations explicitly and reconcile with receipts/trace evidence.

Address-label observations need chain/address, label kind (`ens`, `provider_nametag`, `analyst_note`), value, source/reference, retrieval and source-update times, rights/retention reference and verification state. Never overwrite a provider claim with an analyst's conclusion; keep conflicts and stale labels. ENS is not proof of a legal identity. Private ASPYP mappings stay outside the public package.

## 3. Start with one bounded mainnet pilot

Use a small, explicit Ethereum mainnet address/time allowlist. Confirm key entitlements without printing credentials. Page at most 1,000 records on Free, split bounded block windows, throttle globally per key and honor endpoint-specific caps. Handle retries with finite budgets; store checkpoints and coverage gaps, not a misleading empty history. Deduplicate overlapping windows and revalidate recent blocks for reorgs.

Expected result: a reproducible local observation set with a coverage manifest and no fund movement. Validate transfer totals and event identities against independent receipts for the pilot. Add paid-only BSC/Base once plan and source rights are confirmed; avoid assuming all supported networks are free.

## 4. Add labels and other chains deliberately

For known ENS names, use forward resolution; arbitrary-address discovery requires a separate reverse-resolution strategy with forward confirmation. For provider nametags use Pro Plus, or Enterprise export where licensed. Keep signed export URLs and API keys outside stored public references.

TRON requires its own TRONSCAN/TronGrid provider, address validation, chain namespace, timestamp conversion and TRC-20 event schema. A wrapped token on an EVM network does not prove the original TRON movement. Cross-chain flows require cited bridge events and explicit correlation; address-string similarity alone is insufficient.

## 5. Release evidence-backed generic primitives

Publish only independently written schemas/adapters, deterministic transforms, synthetic tests and redistributable fixtures. Add pagination/quota/reorg/error tests before calling an adapter complete. A code release and a dataset release have separate versions, rights manifests and validation. Review generic graph/dataset work independently from private risk, reputation and recovery logic.
