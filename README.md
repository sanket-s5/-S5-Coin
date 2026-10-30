# S5 Coin (S5) — S5-Tech

**Status: planning / prototype scaffold only. Not a live cryptocurrency.**

S5 Coin is intended to become an independent, Bitcoin-like proof-of-work blockchain.
This repository currently contains project documentation and a draft parameter proposal.
It does **not** contain a working blockchain, wallet, miner, node software, genesis block,
or spendable S5 coins.

## Proposed network parameters

See [`docs/consensus-draft.md`](docs/consensus-draft.md). These values are proposals,
not implemented consensus rules.

## Project principles

- Open development and reproducible builds.
- Transparent supply and founder allocation.
- Testnet before any mainnet launch.
- Independent nodes and peer review before public use.
- Never ask users to send funds to claim, mine, or activate S5.

## Roadmap

1. Review and freeze a written consensus specification.
2. Select and pin an upstream Bitcoin Core release/commit; review its license.
3. Implement S5-specific consensus and network parameters in a dedicated fork.
4. Add unit, functional, regression, fuzz, and compatibility tests.
5. Launch a clearly labelled private testnet; publish source and reproducible build steps.
6. Invite independent node operators and security reviewers.
7. Consider mainnet only after independent review and legal assessment.

## Important

A coin's proposed supply or founder allocation does not create market value. There is no
guarantee of exchange listing, buyers, liquidity, adoption, or profit. Do not advertise
S5 as an investment or promise returns. Obtain qualified legal advice before public
distribution, fundraising, or exchange activity, including advice relevant to India.
