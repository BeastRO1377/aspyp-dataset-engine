# EVM transfer schema v1

`aspyp.datasets.normalize_evm_transfer` transforms one adapter-produced observation into a
`NormalizedTransfer`. The normalizer is deterministic and performs no network access.

## Input contract

| Field | Type | Constraint |
| --- | --- | --- |
| `chain_id` | integer or decimal string | Positive EVM chain identifier. |
| `transaction_hash` | string | 32-byte `0x`-prefixed hex hash. |
| `event_index` | string | Non-empty stable identifier within the transaction. |
| `block_number` | integer or decimal string | Non-negative block number. |
| `block_timestamp` | Unix seconds or RFC 3339 string | RFC 3339 values must contain a timezone. |
| `transfer_type` | string | `native`, `internal_native`, or `erc20`. |
| `from_address`, `to_address` | string | 20-byte `0x`-prefixed EVM addresses. Stored lowercase. |
| `asset_contract` | string or null | Required for `erc20`; null for native transfer types. |
| `asset_symbol` | string | Non-empty display symbol. |
| `asset_decimals` | integer or decimal string | Between 0 and 255. |
| `amount_raw` | integer or decimal string | Non-negative base-unit amount. Never a float. |
| `source_name`, `source_reference` | string | Non-empty provenance identifiers. |

## Output guarantees

- `schema_version` is `evm-transfer/v1`.
- Addresses and transaction hashes are lowercase for deterministic identity.
- `amount_raw` remains an integer in memory and becomes a decimal string in `to_record()`.
- The schema records an observation; it does not claim ownership, intent, risk, legality, or
  beneficiary identity.

## Adapter boundary

An adapter may translate RPC, indexer, archive-node, or public-file data into this contract. It
must keep API keys, source-specific retry policy, raw payload retention, database storage, and
any private attribution outside this package.

## Identity and execution evidence

Use `(chain_id, transaction_hash, transfer_type, event_index)` as the transfer observation key. An ERC-20 event index must identify the actual log, not the transaction's position in the block. Internal transfers require a stable trace identifier. If a provider omits this identity, enrich from a receipt/trace source or mark the observation incomplete; never invent an index that could silently merge events.

Adapters must exclude reverted value movements and record execution status, block hash, acquisition time and finality in their surrounding evidence envelope. This schema validates structure only, not onchain authenticity or execution success. Token symbols and decimals are source claims, not independently verified facts.

RFC 3339 input must include a time, seconds and UTC offset. Leap seconds are not supported. Fractional seconds are truncated to Unix seconds; timestamps before the Unix epoch are rejected. Numeric strings contain ASCII decimal digits only. Integers and integer strings are limited to 4,096 decimal digits for predictable JSON serialization under standard Python settings.
