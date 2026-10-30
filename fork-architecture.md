# S5 Bitcoin Core Fork Architecture — Draft

## Goal

Create a separately identified S5 full-node implementation by modifying a reviewed Bitcoin Core codebase. Keep upstream changes small, documented, and easy to compare. Do not claim Bitcoin Core compatibility until interoperability and consensus tests prove it.

## Repository layout target

```text
S5-Coin/
├── README.md
├── COPYING
├── CONTRIBUTING.md
├── SECURITY.md
├── doc/
│   ├── s5-consensus-spec.md
│   ├── s5-fork-architecture.md
│   ├── s5-test-plan.md
│   └── upstream-update-policy.md
├── src/
│   ├── chainparams.cpp          # S5 main/test/regtest parameters
│   ├── consensus/               # subsidy, retarget and validation changes
│   ├── validation.cpp           # block/transaction validation integration
│   ├── kernel/                  # chainwork and PoW integration
│   └── ...                      # remaining upstream Bitcoin Core source
├── test/
│   ├── functional/
│   ├── fuzz/
│   └── ...                      # upstream tests plus S5-specific cases
├── contrib/
│   └── ...                      # build/release helpers
├── share/
│   └── ...                      # icons and desktop integration
└── release/
    ├── reproducible-builds.md
    └── checksums/
```

This is a target layout, not a directory tree already implemented in the repository. Exact source paths can change between upstream releases.

## Core engineering principles

1. Select a currently maintained upstream Bitcoin Core release/commit and record the exact commit hash.
2. Preserve upstream copyright and license notices. Review the upstream license and all dependency licenses before redistribution.
3. Keep an `UPSTREAM.md` or equivalent recording the upstream commit, local patch list, and merge/rebase procedure.
4. Implement S5-specific chain parameters in one clearly documented area where possible.
5. Keep consensus changes minimal. Avoid unrelated wallet/UI changes in the first milestone.
6. Add consensus test vectors before enabling a rule on any public network.
7. Use deterministic, reproducible builds and publish source hashes and release signatures.
8. Never reuse Bitcoin mainnet magic bytes, ports, address prefixes, genesis hash, or seed infrastructure.
9. Never hard-code founder, treasury, or developer private keys.
10. Do not launch until independent nodes can independently validate the same chain.

## First milestone

The first milestone is a local regtest-like S5 development chain with:
- S5 chain identity;
- configurable fast blocks for tests only;
- 30 S5 subsidy and halving tests;
- difficulty retarget tests;
- max-money and overflow tests;
- UTXO spend tests;
- founder allocation/vesting boundary tests.

Only after those tests pass should a private multi-node testnet be considered.
