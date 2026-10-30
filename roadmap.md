# Development Roadmap

## Phase 0 — Specification
- [ ] Confirm project name, ticker, supply, reward schedule, and allocation mechanism.
- [ ] Publish consensus and network specification.
- [ ] Review jurisdictional obligations and open-source licensing.

## Phase 1 — Source fork
- [ ] Select a stable upstream Bitcoin Core release and record its exact commit.
- [ ] Create a clean fork with upstream attribution and license notices intact.
- [ ] Change chain parameters only after specification review.
- [ ] Keep upstream changes isolated and documented.

## Phase 2 — Private testnet
- [ ] Generate and independently verify genesis block.
- [ ] Run at least three independently controlled nodes.
- [ ] Test mining, difficulty changes, halving boundaries, reorgs, and invalid blocks.
- [ ] Test wallet creation, backup, restore, send, receive, and fee handling.
- [ ] Publish testnet explorer and faucet only after abuse controls are designed.

## Phase 3 — Review
- [ ] Automated tests and fuzzing.
- [ ] Independent security review.
- [ ] Reproducible build verification.
- [ ] Threat model and incident-response plan.
- [ ] Public testnet period with no real-money claims.

## Phase 4 — Mainnet decision
- [ ] Independent review findings resolved.
- [ ] Legal review completed.
- [ ] Node operators and infrastructure documented.
- [ ] Genesis allocation independently verified.
- [ ] Clear launch communication; no investment or profit promises.
