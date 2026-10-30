# S5 Consensus Specification — Draft 0.1

**Not implemented. Do not use these values to run a public network.**

| Parameter | Draft proposal |
|---|---:|
| Name / ticker | S5 Coin / S5 |
| Maximum monetary supply | 21,000,000 S5 |
| Smallest unit | 0.00000001 S5 (1 satoshi-style unit) |
| Target block interval | 600 seconds |
| Initial subsidy | 50 S5 per block |
| Subsidy halving interval | 210,000 blocks |
| Consensus family | Proof of Work |
| Founder allocation target | 6,300,000 S5 (30%) |
| Mining allocation target | 12,600,000 S5 (60%) |
| Community allocation target | 2,100,000 S5 (10%) |
| Founder vesting proposal | 2-year lock, then gradual release |

## Decisions still required

Before coding consensus, the project must explicitly decide and document:

- Exact PoW algorithm, parameters, and ASIC-resistance expectations (if any).
- Difficulty adjustment algorithm and edge-case handling.
- Genesis timestamp, output allocation, merkle root, nonce, and target.
- Exact mechanism for founder/community allocations and vesting.
- Whether allocations are outputs in genesis, scheduled subsidy, or another
  consensus-enforced mechanism. No off-chain promise is sufficient.
- Network magic bytes, P2P port, RPC port, address prefixes, Bech32 HRP,
  message start strings, seed-node policy, and chain identifiers.
- Transaction format, fee policy, dust rules, script/witness support, and upgrade rules.
- Checkpoint policy, reorg limits, activation mechanism, and emergency response.
- Wallet derivation standards, backup/restore behavior, and hardware-wallet support.

## Supply arithmetic

The three proposed buckets add up to 21,000,000 S5:
- Founder: 6,300,000 S5
- Mining: 12,600,000 S5
- Community: 2,100,000 S5

The proposed 50 S5 subsidy halving every 210,000 blocks is Bitcoin-like, but the exact
cumulative mining issuance and allocation mechanism must be modelled and tested before
the monetary schedule can be considered final. Do not assume the proposed bucket split
is automatically compatible with the block subsidy schedule.
