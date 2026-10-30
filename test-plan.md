# S5 Test Plan — Draft

## Consensus arithmetic tests

- Verify 30 S5 initial subsidy in integer base units.
- Verify halving at the exact intended height boundaries.
- Verify integer truncation and the 32 positive subsidy eras.
- Verify cumulative scheduled subsidy equals 12,599,999.9748 S5.
- Verify no block can claim more than subsidy plus valid transaction fees.
- Verify no money-range overflow or total issuance above 21 million S5.

## Difficulty tests

- Retarget after exactly 2,016 blocks.
- Fast blocks trigger harder difficulty.
- Slow blocks trigger easier difficulty.
- Actual timespan clamp is 1/4× to 4× target timespan.
- Test timestamps at boundary values and malformed compact targets.
- Verify proof-of-work limit and chainwork selection.

## Founder vesting tests

- No tranche spendable before the 12-month cliff.
- First 87,500 S5 tranche spendable only at its published UTC unlock time.
- Each later tranche unlocks only at its own published time.
- Exactly 36 tranches total 3,150,000 S5.
- Unauthorized keys cannot spend locked tranches.
- Reorgs and timestamp edge cases do not bypass locks.

## Network and wallet tests

- Distinct S5 network magic, ports, address prefixes and genesis hash.
- Nodes reject malformed blocks and invalid transactions.
- Double-spend attempts are rejected.
- Wallet backup and restore are tested.
- Peer discovery and block propagation work across independent nodes.
- Nodes built from the published source independently agree on consensus.

## Security gates

- Unit, functional, regression and fuzz testing.
- Static analysis and dependency review.
- Independent consensus/code audit.
- Reproducible build verification.
- Private testnet soak period and incident-response plan.
- Legal review before any public distribution or mainnet launch.
