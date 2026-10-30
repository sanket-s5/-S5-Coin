# S5 Coin (S5) — Bitcoin-style fork blueprint

**Status: documentation and configuration scaffold only. No working S5 node, miner, wallet, genesis block, or spendable S5 exists.**

This package records the proposed design for an independent SHA-256 Proof-of-Work blockchain based on a reviewed Bitcoin Core release. It is not a Bitcoin Core source-code fork and is not ready for mainnet.

## Agreed design draft

- Maximum supply: 21,000,000 S5
- Founder allocation: 3,150,000 S5 (15%), subject to 12-month cliff then 36 monthly releases of 87,500 S5
- Mining allocation: 60%, target approximately 12,599,999.9748 S5 under the specified subsidy schedule
- Community allocation: 20% (4,200,000 S5)
- Treasury allocation: 5% (1,050,000 S5)
- SHA-256d Proof of Work
- 10-minute target block interval
- 30 S5 initial block subsidy
- Halving every 210,000 blocks
- Difficulty retarget every 2,016 blocks, Bitcoin-style 4x adjustment bounds
- UTXO transaction model; no staking

## Important unresolved launch decisions

1. Choose and pin an exact upstream Bitcoin Core release/commit only after reviewing its current security status, build process, and license.
2. Decide the exact founder vesting calendar timestamps and how monthly time locks are represented in consensus-valid spendable outputs.
3. Design a transparent, consensus-enforced allocation mechanism. Bitcoin's original genesis coinbase output is not spendable in the ordinary way; do not assume a founder allocation placed there can be spent.
4. Define community and treasury custody, distribution rules, and governance before coding.
5. Choose unique S5 network magic, ports, address prefixes, Bech32 HRP, genesis parameters, seed infrastructure, and chain identifiers.
6. Independently review the subsidy arithmetic, difficulty rules, timestamp rules, and all monetary range checks.

## Build status

This archive contains planning documents and example configuration only. It does not contain Bitcoin Core source code, compiled binaries, wallet software, mining software, or a live network.

Do not send funds to anyone claiming to sell, activate, list, or unlock S5. Do not publish a mainnet launch date until independent review and legal review are complete.
