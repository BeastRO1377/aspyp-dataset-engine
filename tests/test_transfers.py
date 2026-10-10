from __future__ import annotations

import pytest

from aspyp.datasets import EvmTransferType, NormalizationError, normalize_evm_transfer


def valid_observation(**overrides: object) -> dict[str, object]:
    observation: dict[str, object] = {
        "chain_id": 1,
        "transaction_hash": "0x" + "A" * 64,
        "event_index": "17",
        "block_number": "23000000",
        "block_timestamp": "2026-10-07T00:00:00Z",
        "transfer_type": "erc20",
        "from_address": "0x" + "B" * 40,
        "to_address": "0x" + "C" * 40,
        "asset_contract": "0x" + "D" * 40,
        "asset_symbol": "TEST",
        "asset_decimals": 6,
        "amount_raw": "123456789012345678901234567890",
        "source_name": "synthetic-fixture",
        "source_reference": "fixture:erc20:17",
    }
    observation.update(overrides)
    return observation


def test_normalizes_erc20_observation_without_float_conversion():
    transfer = normalize_evm_transfer(valid_observation())

    assert transfer.schema_version == "evm-transfer/v1"
    assert transfer.transfer_type is EvmTransferType.ERC20
    assert transfer.transaction_hash == "0x" + "a" * 64
    assert transfer.from_address == "0x" + "b" * 40
    assert transfer.amount_raw == 123456789012345678901234567890
    assert transfer.block_timestamp == 1791331200
    assert transfer.to_record()["amount_raw"] == "123456789012345678901234567890"


def test_accepts_native_transfer_without_token_contract():
    transfer = normalize_evm_transfer(
        valid_observation(transfer_type="native", asset_contract=None, asset_symbol="ETH", asset_decimals=18)
    )

    assert transfer.transfer_type is EvmTransferType.NATIVE
    assert transfer.asset_contract is None


@pytest.mark.parametrize(
    ("overrides", "message"),
    [
        ({"asset_contract": None}, "ERC-20 transfers require asset_contract"),
        ({"transfer_type": "native"}, "native transfers must not define asset_contract"),
        ({"from_address": "0x1234"}, "from_address must be a 20-byte EVM address"),
        ({"amount_raw": 1.5}, "amount_raw must be a base-10 integer or integer string"),
        ({"block_timestamp": "2026-10-07T00:00:00"}, "must include a timezone"),
        ({"block_timestamp": "1969-12-31T23:59:59Z"}, "must not be negative"),
        ({"block_timestamp": "2026-10-07 00:00:00Z"}, "must be RFC 3339"),
        ({"block_timestamp": True}, "must be Unix seconds"),
        ({"amount_raw": "１２３"}, "must be a base-10 integer"),
        ({"amount_raw": "9" * 5000}, "exceeds the supported integer size"),
        ({"amount_raw": 10**5000}, "exceeds the supported integer size"),
        ({"block_timestamp": "2026-10-07T00:00:00+00:99"}, "must be RFC 3339"),
    ],
)
def test_rejects_ambiguous_or_invalid_observations(overrides: dict[str, object], message: str):
    with pytest.raises(NormalizationError, match=message):
        normalize_evm_transfer(valid_observation(**overrides))


def test_internal_transfer_retains_trace_identity():
    transfer = normalize_evm_transfer(
        valid_observation(
            transfer_type="internal_native",
            asset_contract=None,
            event_index="trace:0_1",
            block_timestamp="2026-10-07T03:00:00+03:00",
        )
    )
    assert transfer.event_index == "trace:0_1"
    assert transfer.block_timestamp == 1791331200
