"""Offline normalization example using entirely synthetic identifiers."""

import json

from aspyp.datasets import normalize_evm_transfer

transfer = normalize_evm_transfer(
    {
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
    }
)
print(json.dumps(transfer.to_record(), indent=2))
