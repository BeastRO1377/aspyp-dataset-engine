"""Provider-neutral normalization for EVM value-transfer observations."""

from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from enum import StrEnum
from typing import Any

_ADDRESS_PATTERN = re.compile(r"0x[0-9a-fA-F]{40}\Z")
_HASH_PATTERN = re.compile(r"0x[0-9a-fA-F]{64}\Z")
_TIMESTAMP_PATTERN = re.compile(
    r"\d{4}-\d{2}-\d{2}[Tt]\d{2}:\d{2}:\d{2}(?:\.\d+)?"
    r"(?:[Zz]|[+-](?:[01]\d|2[0-3]):[0-5]\d)\Z",
    re.ASCII,
)
_MAX_INTEGER = 10**4096


class NormalizationError(ValueError):
    """Raised when an observation cannot be represented by the public schema."""


class EvmTransferType(StrEnum):
    """Value-transfer categories that retain their execution origin."""

    NATIVE = "native"
    INTERNAL_NATIVE = "internal_native"
    ERC20 = "erc20"


@dataclass(frozen=True, slots=True)
class NormalizedTransfer:
    """A source-backed, provider-neutral EVM transfer observation."""

    schema_version: str
    chain_id: int
    transaction_hash: str
    event_index: str
    block_number: int
    block_timestamp: int
    transfer_type: EvmTransferType
    from_address: str
    to_address: str
    asset_contract: str | None
    asset_symbol: str
    asset_decimals: int
    amount_raw: int
    source_name: str
    source_reference: str

    def to_record(self) -> dict[str, Any]:
        """Return a JSON-safe public record without converting amounts to floats."""

        record = asdict(self)
        record["transfer_type"] = self.transfer_type.value
        record["amount_raw"] = str(self.amount_raw)
        return record


def normalize_evm_transfer(observation: Mapping[str, object]) -> NormalizedTransfer:
    """Validate and normalize one provider-adapted EVM transfer observation.

    Adapters are responsible for translating source-specific payloads into this public
    field contract. This function never performs network access, classification, or
    risk scoring.
    """

    transfer_type = _transfer_type(_required_text(observation, "transfer_type"))
    asset_contract = _optional_address(observation.get("asset_contract"), "asset_contract")
    if transfer_type is EvmTransferType.ERC20 and asset_contract is None:
        raise NormalizationError("ERC-20 transfers require asset_contract")
    if transfer_type is not EvmTransferType.ERC20 and asset_contract is not None:
        raise NormalizationError("native transfers must not define asset_contract")

    return NormalizedTransfer(
        schema_version="evm-transfer/v1",
        chain_id=_positive_integer(observation.get("chain_id"), "chain_id"),
        transaction_hash=_hash(_required_text(observation, "transaction_hash")),
        event_index=_required_text(observation, "event_index"),
        block_number=_nonnegative_integer(observation.get("block_number"), "block_number"),
        block_timestamp=_timestamp(observation.get("block_timestamp")),
        transfer_type=transfer_type,
        from_address=_address(_required_text(observation, "from_address"), "from_address"),
        to_address=_address(_required_text(observation, "to_address"), "to_address"),
        asset_contract=asset_contract,
        asset_symbol=_required_text(observation, "asset_symbol"),
        asset_decimals=_bounded_integer(observation.get("asset_decimals"), "asset_decimals", 0, 255),
        amount_raw=_nonnegative_integer(observation.get("amount_raw"), "amount_raw"),
        source_name=_required_text(observation, "source_name"),
        source_reference=_required_text(observation, "source_reference"),
    )


def _transfer_type(value: str) -> EvmTransferType:
    try:
        return EvmTransferType(value)
    except ValueError as exc:
        allowed = ", ".join(item.value for item in EvmTransferType)
        raise NormalizationError(f"transfer_type must be one of: {allowed}") from exc


def _required_text(observation: Mapping[str, object], field: str) -> str:
    value = observation.get(field)
    if not isinstance(value, str) or not value.strip():
        raise NormalizationError(f"{field} must be a non-empty string")
    return value.strip()


def _address(value: str, field: str) -> str:
    if not _ADDRESS_PATTERN.fullmatch(value):
        raise NormalizationError(f"{field} must be a 20-byte EVM address")
    return value.lower()


def _optional_address(value: object, field: str) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str):
        raise NormalizationError(f"{field} must be a 20-byte EVM address or null")
    return _address(value, field)


def _hash(value: str) -> str:
    if not _HASH_PATTERN.fullmatch(value):
        raise NormalizationError("transaction_hash must be a 32-byte EVM transaction hash")
    return value.lower()


def _positive_integer(value: object, field: str) -> int:
    result = _integer(value, field)
    if result < 1:
        raise NormalizationError(f"{field} must be positive")
    return result


def _nonnegative_integer(value: object, field: str) -> int:
    result = _integer(value, field)
    if result < 0:
        raise NormalizationError(f"{field} must not be negative")
    return result


def _bounded_integer(value: object, field: str, minimum: int, maximum: int) -> int:
    result = _integer(value, field)
    if not minimum <= result <= maximum:
        raise NormalizationError(f"{field} must be between {minimum} and {maximum}")
    return result


def _integer(value: object, field: str) -> int:
    if isinstance(value, bool):
        raise NormalizationError(f"{field} must be an integer")
    if isinstance(value, int):
        if abs(value) >= _MAX_INTEGER:
            raise NormalizationError(f"{field} exceeds the supported integer size")
        return value
    if isinstance(value, str) and value.isascii() and value.isdecimal():
        if len(value) > 4096:
            raise NormalizationError(f"{field} exceeds the supported integer size")
        try:
            return int(value)
        except ValueError as exc:
            raise NormalizationError(f"{field} exceeds the supported integer size") from exc
    raise NormalizationError(f"{field} must be a base-10 integer or integer string")


def _timestamp(value: object) -> int:
    if isinstance(value, int) and not isinstance(value, bool):
        return _nonnegative_integer(value, "block_timestamp")
    if isinstance(value, str) and value.isascii() and value.isdecimal():
        return _nonnegative_integer(value, "block_timestamp")
    if isinstance(value, str):
        if not _TIMESTAMP_PATTERN.fullmatch(value):
            raise NormalizationError("block_timestamp must be RFC 3339 and must include a timezone")
        try:
            parsed = datetime.fromisoformat(value.upper())
        except ValueError as exc:
            raise NormalizationError("block_timestamp must be Unix seconds or an RFC 3339 timestamp") from exc
        if parsed.tzinfo is None:
            raise NormalizationError("block_timestamp RFC 3339 timestamps must include a timezone")
        timestamp = parsed.astimezone(UTC).timestamp()
        if timestamp < 0:
            raise NormalizationError("block_timestamp must not be negative")
        return int(timestamp)
    raise NormalizationError("block_timestamp must be Unix seconds or an RFC 3339 timestamp")
