# ASPYP Dataset Engine

[![Package checks](https://github.com/BeastRO1377/aspyp-dataset-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/BeastRO1377/aspyp-dataset-engine/actions/workflows/ci.yml)

A dependency-free, provider-neutral Python core for EVM transfer normalization and source provenance.

## Status

Version 0.2.0 implements `evm-transfer/v1` normalization for native, internal native and ERC-20 transfers. Evidence, entities, graph and API modules are architectural placeholders; collectors, persistent storage, graph traversal, attribution and an investigation service are not implemented in this release.

The intended pipeline is **Sources → Evidence → Entities → Graph → Dataset → Analysis**. The core accepts independently sourced, adapter-produced observations. It requires neither a private ASPYP service nor a network credential.

## Install

Python 3.11 or newer:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install "git+https://github.com/BeastRO1377/aspyp-dataset-engine.git@v0.2.0"
python -c "import aspyp; print(aspyp.__version__)"
```

This is a GitHub source release; no PyPI publication is claimed.

## Offline example

```python
from aspyp.datasets import normalize_evm_transfer

transfer = normalize_evm_transfer({
    "chain_id": 1,
    "transaction_hash": "0x" + "a" * 64,
    "event_index": "log:17",
    "block_number": 23000000,
    "block_timestamp": "2026-10-07T00:00:00Z",
    "transfer_type": "erc20",
    "from_address": "0x" + "b" * 40,
    "to_address": "0x" + "c" * 40,
    "asset_contract": "0x" + "d" * 40,
    "asset_symbol": "TEST",
    "asset_decimals": 6,
    "amount_raw": "123456789012345678901234567890",
    "source_name": "synthetic-example",
    "source_reference": "fixture:erc20:17",
})
assert transfer.to_record()["amount_raw"] == "123456789012345678901234567890"
```

All example identifiers are synthetic. Run `python examples/normalize_transfer.py` after installation for JSON output.

## Development and validation

```sh
python -m pip install ".[dev]" build twine
python -m pytest -q
python -m ruff check .
python -m build
python -m twine check dist/*
```

Use a normal package or wheel installation to validate distribution imports. An editable installation can depend on local `.pth` handling; `PYTHONPATH=src` alone does not prove that a published package works.

## Public and private boundaries

Public: neutral schemas, deterministic normalization, provenance contracts, synthetic fixtures and technical documentation. Planned extensions include generic adapters, graph structures and dataset transformations.

Private: real ASPYP datasets, entity-resolution mappings, behavioural models, reputation data, commercial risk formulas, inference rules, payment/authorization/settlement/recovery mechanisms, credentials and production state.

Mainnet observation and testnet payment experiments are separate concerns. This package neither sends transactions nor manages funds. TRON/TRC-20 is outside the EVM schema and needs its own adapter and schema.

## Documentation

- [Transfer schema](docs/evm-transfer-schema.md)
- [Architecture](docs/architecture.md)
- [Etherscan capability review, 2026-10-10](docs/etherscan-capabilities-2026-10-10.md)
- [Endpoint inventory](docs/etherscan-endpoints-2026-10-10.md)
- [Network inventory](docs/etherscan-networks-2026-10-10.md)
- [Mainnet investigation roadmap](docs/mainnet-investigation-roadmap.md)
- [Changelog](CHANGELOG.md)

## License and data rights

The code is licensed under [Apache-2.0](LICENSE); see [NOTICE](NOTICE). The software license grants no rights to third-party datasets, labels, contract sources or API responses. No real address-label export is bundled. Provider access, commercial use, retention and redistribution must be assessed under the source's own terms before ingestion or publication.
