# S5 Consensus Specification — Draft 0.3

## 1. Monetary units

- Ticker: S5
- Precision: 8 decimal places
- One S5 = 100,000,000 base units
- Maximum money: 2,100,000,000,000,000 base units (21 million S5)
- All arithmetic in consensus code must use integer base units; floating-point arithmetic is prohibited.

## 2. Proof of Work

- Algorithm: SHA-256d (double SHA-256 of the serialized block header, Bitcoin-style)
- Target block interval: 600 seconds
- Target timespan: 1,209,600 seconds (14 days)
- Retarget interval: 2,016 blocks
- Retarget clamp: actual timespan constrained to one-quarter through four times the target timespan, matching Bitcoin's traditional retarget clamp
- Proof-of-work target must never exceed the network's configured proof-of-work limit.
- The exact genesis target, compact target encoding, chainwork calculation, timestamp validation and test vectors must be specified before implementation.

## 3. Subsidy schedule

Initial subsidy: 30 S5 per block = 3,000,000,000 base units.

At each height divisible by 210,000, the subsidy is integer-divided by two in base units. Subsidy becomes zero when integer division reaches zero. This produces 32 positive subsidy eras.

With 210,000 blocks per era and integer base-unit halving:
- Total scheduled mining subsidy: 1,259,999,997,480,000 base units
- Total scheduled mining subsidy: 12,599,999.9748 S5
- Unissued difference from the 12,600,000 S5 mining allocation: 0.0252 S5

Transaction fees are not new issuance and must be accounted for separately. Consensus validation must reject any block that claims more than subsidy plus valid fees.

## 4. Proposed allocation plan

| Allocation | Share | Amount |
|---|---:|---:|
| Founder | 15% | 3,150,000 S5 |
| Mining subsidy budget | 60% | 12,600,000 S5 |
| Community | 20% | 4,200,000 S5 |
| Treasury | 5% | 1,050,000 S5 |
| Total | 100% | 21,000,000 S5 |

The mining schedule actually emits approximately 12,599,999.9748 S5; the 0.0252 S5 difference remains unissued. Therefore, the maximum supply is a ceiling, not a promise that every last base unit will be created.

## 5. Founder vesting — proposed

- Founder allocation: 3,150,000 S5.
- Cliff: 12 months from the agreed vesting start timestamp.
- Thereafter: 36 monthly tranches of 87,500 S5 each.
- Total: 87,500 × 36 = 3,150,000 S5.
- Vesting dates must be fixed in advance and published.
- Consensus must enforce each tranche's spend lock; documentation alone is not enforcement.
- Do not rely on a vague “month” calculation in code. Define exact UTC unlock timestamps and the permitted time-lock semantics, and test boundary conditions.
- The founder must control the designated receiving key(s); never commit private keys or seed phrases to the repository.

Important: Bitcoin's genesis coinbase output is not ordinarily spendable. The implementation must use a specifically designed and audited initial allocation mechanism (for example, a consensus-recognized allocation transaction/output at a defined height) rather than assuming a genesis coinbase can be spent. The exact mechanism is unresolved and must be designed before code is written.

## 6. Community and treasury allocations

The 4,200,000 S5 community allocation and 1,050,000 S5 treasury allocation need:
- public receiving addresses or transparent distribution contracts/mechanisms appropriate to the chosen implementation;
- custody and signing policies;
- published release/distribution schedules;
- independent review and audit trail.

Do not put a private key in source code or configuration.

## 7. UTXO transaction model

S5 intends to retain Bitcoin-style UTXO accounting:
- each input references a prior unspent output;
- scripts and signatures authorize spending;
- nodes independently validate scripts, input availability, values, fees and transaction structure;
- double spends are rejected;
- coinbase maturity and standardness policy must be defined;
- money-range checks use integer base units and enforce the 21-million ceiling.

## 8. Parameters still requiring explicit specification

- maximum block weight/size and transaction policy;
- coinbase maturity;
- minimum relay fee and dust policy;
- timestamp/median-time-past rules;
- genesis block fields and proof-of-work limit;
- P2P protocol version and network magic;
- address prefixes and Bech32 HRP;
- activation/deployment mechanism for any future consensus changes;
- testnet/regtest parameters;
- seed nodes and DNS seed operation;
- reorg limits and operational monitoring.

This document is a draft, not implemented consensus code and not a security audit.
