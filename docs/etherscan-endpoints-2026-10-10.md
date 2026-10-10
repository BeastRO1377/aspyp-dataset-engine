# Etherscan endpoint inventory — 2026-10-10

Reviewed all 97 endpoint pages linked by the [official documentation index](https://docs.etherscan.io/llms.txt). Each link below points to the individually reviewed source. This is a documentation review, not a live entitlement test. An unmarked endpoint is not proof of access on every chain or plan. Chain availability and provider terms also apply.

| Endpoint | Documented gate | Selection for investigation work |
| --- | --- | --- |
| [balance](https://docs.etherscan.io/api-reference/endpoint/balance) | No explicit PRO gate found; check chain/plan | Optional enrichment / network context |
| [balancemulti](https://docs.etherscan.io/api-reference/endpoint/balancemulti) | No explicit PRO gate found; check chain/plan | Optional enrichment / network context |
| [balancehistory](https://docs.etherscan.io/api-reference/endpoint/balancehistory) | Standard or higher; 2 requests/s | Optional enrichment / network context |
| [txlist](https://docs.etherscan.io/api-reference/endpoint/txlist) | No explicit PRO gate found; check chain/plan | Transfer or execution evidence; preserve identities |
| [advanced-filter-txlist](https://docs.etherscan.io/api-reference/endpoint/advanced-filter-txlist) | No explicit PRO gate found; check chain/plan; beta | Transfer or execution evidence; preserve identities |
| [tokentx](https://docs.etherscan.io/api-reference/endpoint/tokentx) | No explicit PRO gate found; check chain/plan | Transfer or execution evidence; preserve identities |
| [advanced-filter-tokentx](https://docs.etherscan.io/api-reference/endpoint/advanced-filter-tokentx) | No explicit PRO gate found; check chain/plan; beta | Transfer or execution evidence; preserve identities |
| [tokennfttx](https://docs.etherscan.io/api-reference/endpoint/tokennfttx) | No explicit PRO gate found; check chain/plan | Transfer or execution evidence; preserve identities |
| [advanced-filter-tokennfttx](https://docs.etherscan.io/api-reference/endpoint/advanced-filter-tokennfttx) | No explicit PRO gate found; check chain/plan; beta | Transfer or execution evidence; preserve identities |
| [token1155tx](https://docs.etherscan.io/api-reference/endpoint/token1155tx) | No explicit PRO gate found; check chain/plan | Transfer or execution evidence; preserve identities |
| [advanced-filter-token1155tx](https://docs.etherscan.io/api-reference/endpoint/advanced-filter-token1155tx) | No explicit PRO gate found; check chain/plan; beta | Transfer or execution evidence; preserve identities |
| [txlistinternal](https://docs.etherscan.io/api-reference/endpoint/txlistinternal) | No explicit PRO gate found; check chain/plan | Transfer or execution evidence; preserve identities |
| [advanced-filter-txlistinternal](https://docs.etherscan.io/api-reference/endpoint/advanced-filter-txlistinternal) | No explicit PRO gate found; check chain/plan; beta | Transfer or execution evidence; preserve identities |
| [txlistinternal-blockrange](https://docs.etherscan.io/api-reference/endpoint/txlistinternal-blockrange) | Standard or higher | Transfer or execution evidence; preserve identities |
| [txlistinternal-txhash](https://docs.etherscan.io/api-reference/endpoint/txlistinternal-txhash) | No explicit PRO gate found; check chain/plan | Transfer or execution evidence; preserve identities |
| [getminedblocks](https://docs.etherscan.io/api-reference/endpoint/getminedblocks) | No explicit PRO gate found; check chain/plan | Optional enrichment / network context |
| [txsbeaconwithdrawal](https://docs.etherscan.io/api-reference/endpoint/txsbeaconwithdrawal) | No explicit PRO gate found; check chain/plan | Transfer or execution evidence; preserve identities |
| [fundedby](https://docs.etherscan.io/api-reference/endpoint/fundedby) | Standard or higher; 2 requests/s | Contract / funding context |
| [getblockreward](https://docs.etherscan.io/api-reference/endpoint/getblockreward) | No explicit PRO gate found; check chain/plan | Optional enrichment / network context |
| [getblocktxnscount](https://docs.etherscan.io/api-reference/endpoint/getblocktxnscount) | No explicit PRO gate found; check chain/plan | Transfer or execution evidence; preserve identities |
| [getblockcountdown](https://docs.etherscan.io/api-reference/endpoint/getblockcountdown) | No explicit PRO gate found; check chain/plan | Optional enrichment / network context |
| [getblocknobytime](https://docs.etherscan.io/api-reference/endpoint/getblocknobytime) | No explicit PRO gate found; check chain/plan | Optional enrichment / network context |
| [dailyavgblocksize](https://docs.etherscan.io/api-reference/endpoint/dailyavgblocksize) | Standard or higher | Optional enrichment / network context |
| [dailyblkcount](https://docs.etherscan.io/api-reference/endpoint/dailyblkcount) | Standard or higher | Optional enrichment / network context |
| [dailyblockrewards](https://docs.etherscan.io/api-reference/endpoint/dailyblockrewards) | Standard or higher | Optional enrichment / network context |
| [dailyavgblocktime](https://docs.etherscan.io/api-reference/endpoint/dailyavgblocktime) | Standard or higher | Optional enrichment / network context |
| [dailyuncleblkcount](https://docs.etherscan.io/api-reference/endpoint/dailyuncleblkcount) | Standard or higher | Optional enrichment / network context |
| [getabi](https://docs.etherscan.io/api-reference/endpoint/getabi) | No explicit PRO gate found; check chain/plan | Contract / funding context |
| [getsourcecode](https://docs.etherscan.io/api-reference/endpoint/getsourcecode) | No explicit PRO gate found; check chain/plan | Contract / funding context |
| [getcontractcreation](https://docs.etherscan.io/api-reference/endpoint/getcontractcreation) | No explicit PRO gate found; check chain/plan | Contract / funding context |
| [verifysourcecode](https://docs.etherscan.io/api-reference/endpoint/verifysourcecode) | No explicit PRO gate found; check chain/plan | Contract publication tools; outside collector |
| [verifyzksyncsourcecode](https://docs.etherscan.io/api-reference/endpoint/verifyzksyncsourcecode) | No explicit PRO gate found; check chain/plan | Contract publication tools; outside collector |
| [verifyvyper](https://docs.etherscan.io/api-reference/endpoint/verifyvyper) | No explicit PRO gate found; check chain/plan | Contract publication tools; outside collector |
| [verifystylus](https://docs.etherscan.io/api-reference/endpoint/verifystylus) | No explicit PRO gate found; check chain/plan | Contract publication tools; outside collector |
| [verifyproxycontract](https://docs.etherscan.io/api-reference/endpoint/verifyproxycontract) | No explicit PRO gate found; check chain/plan | Contract publication tools; outside collector |
| [checkverifystatus](https://docs.etherscan.io/api-reference/endpoint/checkverifystatus) | No explicit PRO gate found; check chain/plan | Contract publication tools; outside collector |
| [checkproxyverification](https://docs.etherscan.io/api-reference/endpoint/checkproxyverification) | No explicit PRO gate found; check chain/plan | Contract publication tools; outside collector |
| [gasestimate](https://docs.etherscan.io/api-reference/endpoint/gasestimate) | No explicit PRO gate found; check chain/plan | Optional enrichment / network context |
| [gasoracle](https://docs.etherscan.io/api-reference/endpoint/gasoracle) | No explicit PRO gate found; check chain/plan | Optional enrichment / network context |
| [dailyavggaslimit](https://docs.etherscan.io/api-reference/endpoint/dailyavggaslimit) | Standard or higher | Optional enrichment / network context |
| [dailygasused](https://docs.etherscan.io/api-reference/endpoint/dailygasused) | Standard or higher | Optional enrichment / network context |
| [dailyavggasprice](https://docs.etherscan.io/api-reference/endpoint/dailyavggasprice) | Standard or higher | Optional enrichment / network context |
| [ethblocknumber](https://docs.etherscan.io/api-reference/endpoint/ethblocknumber) | No explicit PRO gate found; check chain/plan | Optional enrichment / network context |
| [ethgetblockbynumber](https://docs.etherscan.io/api-reference/endpoint/ethgetblockbynumber) | No explicit PRO gate found; check chain/plan | Optional enrichment / network context |
| [ethgetunclebyblocknumberandindex](https://docs.etherscan.io/api-reference/endpoint/ethgetunclebyblocknumberandindex) | No explicit PRO gate found; check chain/plan | Optional enrichment / network context |
| [ethgetblocktransactioncountbynumber](https://docs.etherscan.io/api-reference/endpoint/ethgetblocktransactioncountbynumber) | No explicit PRO gate found; check chain/plan | Optional enrichment / network context |
| [ethgettransactionbyhash](https://docs.etherscan.io/api-reference/endpoint/ethgettransactionbyhash) | No explicit PRO gate found; check chain/plan | Transfer or execution evidence; preserve identities |
| [ethgettransactionbyblocknumberandindex](https://docs.etherscan.io/api-reference/endpoint/ethgettransactionbyblocknumberandindex) | No explicit PRO gate found; check chain/plan | Transfer or execution evidence; preserve identities |
| [ethgettransactioncount](https://docs.etherscan.io/api-reference/endpoint/ethgettransactioncount) | No explicit PRO gate found; check chain/plan | Transfer or execution evidence; preserve identities |
| [ethsendrawtransaction](https://docs.etherscan.io/api-reference/endpoint/ethsendrawtransaction) | No explicit PRO gate found; check chain/plan | Broadcasts a transaction; exclude from read-only collector |
| [ethgettransactionreceipt](https://docs.etherscan.io/api-reference/endpoint/ethgettransactionreceipt) | No explicit PRO gate found; check chain/plan | Transfer or execution evidence; preserve identities |
| [ethcall](https://docs.etherscan.io/api-reference/endpoint/ethcall) | No explicit PRO gate found; check chain/plan | Optional enrichment / network context |
| [ethgetcode](https://docs.etherscan.io/api-reference/endpoint/ethgetcode) | No explicit PRO gate found; check chain/plan | Optional enrichment / network context |
| [ethgetstorageat](https://docs.etherscan.io/api-reference/endpoint/ethgetstorageat) | No explicit PRO gate found; check chain/plan | Optional enrichment / network context |
| [ethgasprice](https://docs.etherscan.io/api-reference/endpoint/ethgasprice) | No explicit PRO gate found; check chain/plan | Optional enrichment / network context |
| [ethestimategas](https://docs.etherscan.io/api-reference/endpoint/ethestimategas) | No explicit PRO gate found; check chain/plan | Optional enrichment / network context |
| [getlogs](https://docs.etherscan.io/api-reference/endpoint/getlogs) | No explicit PRO gate found; check chain/plan | Transfer or execution evidence; preserve identities |
| [getlogs-topics](https://docs.etherscan.io/api-reference/endpoint/getlogs-topics) | No explicit PRO gate found; check chain/plan | Transfer or execution evidence; preserve identities |
| [getlogs-address-topics](https://docs.etherscan.io/api-reference/endpoint/getlogs-address-topics) | No explicit PRO gate found; check chain/plan | Transfer or execution evidence; preserve identities |
| [ethsupply](https://docs.etherscan.io/api-reference/endpoint/ethsupply) | No explicit PRO gate found; check chain/plan | Optional enrichment / network context |
| [ethsupply2](https://docs.etherscan.io/api-reference/endpoint/ethsupply2) | No explicit PRO gate found; check chain/plan | Optional enrichment / network context |
| [ethprice](https://docs.etherscan.io/api-reference/endpoint/ethprice) | No explicit PRO gate found; check chain/plan | Optional enrichment / network context |
| [chainsize](https://docs.etherscan.io/api-reference/endpoint/chainsize) | No explicit PRO gate found; check chain/plan | Optional enrichment / network context |
| [nodecount](https://docs.etherscan.io/api-reference/endpoint/nodecount) | No explicit PRO gate found; check chain/plan | Optional enrichment / network context |
| [nodecounthistory](https://docs.etherscan.io/api-reference/endpoint/nodecounthistory) | Standard or higher | Optional enrichment / network context |
| [dailytxnfee](https://docs.etherscan.io/api-reference/endpoint/dailytxnfee) | Standard or higher | Transfer or execution evidence; preserve identities |
| [dailynewaddress](https://docs.etherscan.io/api-reference/endpoint/dailynewaddress) | Standard or higher | Optional enrichment / network context |
| [dailyensregister](https://docs.etherscan.io/api-reference/endpoint/dailyensregister) | Standard or higher | Optional enrichment / network context |
| [dailynetutilization](https://docs.etherscan.io/api-reference/endpoint/dailynetutilization) | Standard or higher | Optional enrichment / network context |
| [dailyavghashrate](https://docs.etherscan.io/api-reference/endpoint/dailyavghashrate) | Standard or higher | Optional enrichment / network context |
| [dailytx](https://docs.etherscan.io/api-reference/endpoint/dailytx) | Standard or higher | Transfer or execution evidence; preserve identities |
| [dailyavgnetdifficulty](https://docs.etherscan.io/api-reference/endpoint/dailyavgnetdifficulty) | Standard or higher | Optional enrichment / network context |
| [ethdailyprice](https://docs.etherscan.io/api-reference/endpoint/ethdailyprice) | Standard or higher | Optional enrichment / network context |
| [getstatus](https://docs.etherscan.io/api-reference/endpoint/getstatus) | No explicit PRO gate found; check chain/plan | Transfer or execution evidence; preserve identities |
| [gettxreceiptstatus](https://docs.etherscan.io/api-reference/endpoint/gettxreceiptstatus) | No explicit PRO gate found; check chain/plan | Transfer or execution evidence; preserve identities |
| [tokensupply](https://docs.etherscan.io/api-reference/endpoint/tokensupply) | No explicit PRO gate found; check chain/plan | Optional enrichment / network context |
| [tokensupplyhistory](https://docs.etherscan.io/api-reference/endpoint/tokensupplyhistory) | Standard or higher; 2 requests/s | Optional enrichment / network context |
| [tokenbalance](https://docs.etherscan.io/api-reference/endpoint/tokenbalance) | No explicit PRO gate found; check chain/plan | Optional enrichment / network context |
| [tokenbalancehistory](https://docs.etherscan.io/api-reference/endpoint/tokenbalancehistory) | Standard or higher; 2 requests/s | Optional enrichment / network context |
| [topholders](https://docs.etherscan.io/api-reference/endpoint/topholders) | Standard or higher; 2 requests/s | Optional enrichment / network context |
| [tokenholderlist](https://docs.etherscan.io/api-reference/endpoint/tokenholderlist) | Standard or higher | Optional enrichment / network context |
| [tokenholdercount](https://docs.etherscan.io/api-reference/endpoint/tokenholdercount) | Standard or higher | Optional enrichment / network context |
| [tokeninfo](https://docs.etherscan.io/api-reference/endpoint/tokeninfo) | Standard or higher; 2 requests/s | Optional enrichment / network context |
| [addresstokenbalance](https://docs.etherscan.io/api-reference/endpoint/addresstokenbalance) | Standard or higher; 2 requests/s | Optional enrichment / network context |
| [addresstokennftbalance](https://docs.etherscan.io/api-reference/endpoint/addresstokennftbalance) | Standard or higher; 2 requests/s | Optional enrichment / network context |
| [addresstokennftinventory](https://docs.etherscan.io/api-reference/endpoint/addresstokennftinventory) | Standard or higher; 2 requests/s | Optional enrichment / network context |
| [txnbridge](https://docs.etherscan.io/api-reference/endpoint/txnbridge) | No explicit PRO gate found; check chain/plan | Transfer or execution evidence; preserve identities |
| [getdeposittxs](https://docs.etherscan.io/api-reference/endpoint/getdeposittxs) | No explicit PRO gate found; check chain/plan | Transfer or execution evidence; preserve identities |
| [getwithdrawaltxs](https://docs.etherscan.io/api-reference/endpoint/getwithdrawaltxs) | No explicit PRO gate found; check chain/plan | Transfer or execution evidence; preserve identities |
| [forwardresolve](https://docs.etherscan.io/api-reference/endpoint/forwardresolve) | Ethereum mainnet; Free: 1 request/s | Names/labels; preserve provenance and data rights |
| [getaddresstag](https://docs.etherscan.io/api-reference/endpoint/getaddresstag) | Pro Plus; 2 requests/s | Names/labels; preserve provenance and data rights |
| [getapilimit](https://docs.etherscan.io/api-reference/endpoint/getapilimit) | No explicit PRO gate found; check chain/plan | Coverage / usage monitoring |
| [chainlist](https://docs.etherscan.io/api-reference/endpoint/chainlist) | No explicit PRO gate found; check chain/plan | Coverage / usage monitoring |
| [getlabelmasterlist-v2](https://docs.etherscan.io/api-reference/endpoint/getlabelmasterlist-v2) | Enterprise | Names/labels; preserve provenance and data rights |
| [exportaddresstags-v2](https://docs.etherscan.io/api-reference/endpoint/exportaddresstags-v2) | Enterprise; 2 requests/s, 100/day | Names/labels; preserve provenance and data rights |
| [getlabelmasterlist](https://docs.etherscan.io/api-reference/endpoint/getlabelmasterlist) | Enterprise | Names/labels; preserve provenance and data rights |
| [exportaddresstags](https://docs.etherscan.io/api-reference/endpoint/exportaddresstags) | Enterprise; 2 requests/s, 100/day | Names/labels; preserve provenance and data rights |

[Prediction market APIs](https://docs.etherscan.io/beta/prediction-market) are a separate opt-in beta; do not treat them as stable or include them in the v0.2.0 implementation.
