# Etherscan capability review — 2026-10-10

## Verified scope

One Etherscan V2 key selects supported EVM chains with `chainid`; it does not cover all blockchains. BSC means BNB Smart Chain (56 mainnet, 97 testnet). TRC-20 is a TRON token standard and needs a separate TRON provider. See [Etherscan introduction](https://docs.etherscan.io/introduction), [chainlist](https://api.etherscan.io/v2/chainlist) and [TRONSCAN transfers](https://docs.tronscan.org/en/api/transactions-and-transfers/trc20-transfers-with-status).

Reviewed all 97 endpoint pages from the current official index, plus beta, chain availability, limits, errors, metadata and terms. The [endpoint inventory](etherscan-endpoints-2026-10-10.md) links every reviewed page; the [network inventory](etherscan-networks-2026-10-10.md) records the 63-chain snapshot. No credentialed endpoint requests or account-plan verification were performed.

## Useful capability groups

| Group | Investigation use | Access considerations |
| --- | --- | --- |
| Account transactions | Native movements and account history; normal and internal transactions | Chain eligibility; block-range internal history is PRO |
| ERC-20/721/1155 transfers | Fungible token and NFT flows | Stable log identity and pagination required; advanced filters are beta |
| Logs, transaction receipts and execution status | Verify events, errors and reverted execution | Read-only evidence; do not equate a transaction hash with a unique transfer |
| Contract ABI, source and creator | Decode events, identify deployers and proxy implementations | ABI/source available on Free across supported chains; retrieved code retains its own license |
| Blocks and timestamp lookup | Bound investigations in time and reconcile block identity | Record block hash and finality separately |
| Balances and token supply | Position/context snapshots | Historical values and holder/portfolio endpoints generally require PRO |
| First funder (`fundedby`) | First funding address and transaction for an EOA | Standard+; 2 requests/s; unavailable for contract addresses |
| ENS | Resolve a known onchain name to an address | Ethereum mainnet only; Free 1 request/s |
| Address metadata | Nametags, labels, reputation and source update time | Pro Plus; no coverage guarantee for any particular address |
| Metadata exports | Label catalogue and tagged addresses by label | Enterprise; separate metadata host; exports are not open data |
| L2 deposits/withdrawals | Bridge-related evidence | Endpoint/chain-specific; generic cross-chain attribution is not provided |
| Gas, prices and network statistics | Context for a report | Many historical statistics are PRO; not address attribution |
| Usage and chainlist | Quotas and current coverage | Do not infer plan eligibility solely from chain presence |
| Contract verification and broadcasting | Deployment/transaction operations | Outside the read-only investigation collector |

Detailed gates are linked per endpoint in the inventory. These capabilities are upstream options, not functionality implemented by ASPYP v0.2.0.

## Names are different observations

[ENS forward resolution](https://docs.etherscan.io/api-reference/endpoint/forwardresolve) takes a known name and returns an address. It does not discover names for arbitrary addresses. Results may lag five minutes; offchain CCIP Read/wildcard names are excluded. Reverse discovery requires another source and a forward check.

[Address metadata](https://docs.etherscan.io/api-reference/endpoint/getaddresstag) returns provider-supplied names and labels, with up to 100 addresses per request and a 2 requests/s cap. It is exclusively Pro Plus. A label is a source claim, not proof of identity, control, crime or ownership. Missing labels mean unknown.

[Metadata export](https://docs.etherscan.io/api-reference/endpoint/exportaddresstags-v2) uses `api-metadata.etherscan.io/v2/api`, not the ordinary API host. Enterprise exports produce signed download links valid for five minutes. Limits: 2 requests/s, 100/day. [Label master list](https://docs.etherscan.io/api-reference/endpoint/getlabelmasterlist-v2) supplies label slugs. Do not retain signed URLs in public evidence or assume ordinary-key entitlements include Enterprise export.

## Quotas and recent changes

[Rate limits](https://docs.etherscan.io/rate-limits): Free 3 requests/s and 100,000/day on selected chains; Lite 5/s and 100,000/day; Standard 10/s and 200,000/day; Advanced 20/s and 500,000/day; Professional 30/s and 1,000,000/day; Pro Plus 30/s and 1,500,000/day. PRO methods start at Standard, subject to endpoint exceptions. Network tables currently mark BSC, Base, OP, Avalanche and Gnosis community access as paid-only.

Relevant [changelog](https://docs.etherscan.io/changelog) findings:

- Free history/log pages have a 1,000-record ceiling since July 1; paginate and split block ranges.
- Block-range internal transactions moved to PRO on July 1.
- Minimal proxies use `Proxy=2`; follow `Implementation`, while keeping the proxy's address as its own identity.
- opBNB 204/5611 is deprecated on October 12; do not onboard it for a new collector.
- Arc/Robinhood community methods require Lite+ from October 16; ABI/source remain Free.
- Free Celo, Linea and Katana access uses shared pools; Arbitrum adopts this from November 1.
- Scroll, Swell and Moonbeam/Moonriver coverage was removed earlier in 2026; MemeCore testnet moved to 43522.

[Error handling](https://docs.etherscan.io/common-error-messages) must distinguish quota exhaustion, unsupported chain, invalid key, plan denial and a genuine empty result. HTTP 200 alone is not evidence of success or complete history.

## Code license versus provider data rights

The live [API Terms](https://etherscan.io/apiterms), retrieved on October 10, show **Last updated: October 1, 2026**. Search-engine copies still showed June, so the live text was checked separately.

Free/Lite/Standard permit Personal & Research use; Advanced and higher include Commercial Application use. That includes third-party applications even when free, and organisational use. Display must add “Powered by Etherscan.io APIs” with a link where practicable. Commercial access does not grant permission to distribute a standalone dataset, data feed or API mirror. Bulk replication is restricted. Runtime AI features can be allowed within plan entitlements, but model training, improvement, evaluation datasets and competing data products require a separate written agreement. External sharing and retention beyond permitted periods also require specific rights; no numerical retention allowance was established here.

The [general Terms](https://etherscan.io/terms), live text dated August 13, also restrict label reproduction and dataset creation without prior permission. The practical release boundary is therefore: publish code and synthetic fixtures; obtain written provider approval defining investigation storage, retention, label use, exports and redistribution before creating a redistributable Etherscan-derived dataset. An Enterprise export subscription alone is not proof of redistribution permission.

This review does not confirm this maintainer's plan, key, negotiated licence or access to paid endpoints.
