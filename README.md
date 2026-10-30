# S5 Development Starter — Milestone 1

**Experimental reference code only. This is not a working cryptocurrency node, wallet, miner, or production blockchain.**

Includes:
- `s5/consensus.py`: integer-only reference subsidy and money-range helpers.
- `tests/test_consensus.py`: unit tests.
- `docs/UPSTREAM-BASELINE.md`: proposed Bitcoin Core source baseline.
- `docs/NEXT-STEPS.md`: engineering milestones.

Proposed rules: 8 decimals; 100,000,000 base units per S5; 21,000,000 S5 maximum money ceiling; 30 S5 initial block subsidy; halving every 210,000 blocks; SHA-256d and 600-second target blocks (not implemented here).

Run tests with Python 3.10+:
```bash
python -m unittest discover -s tests -v
```

This package does not include Bitcoin Core source and cannot create or connect to an S5 network. The reference helper must be independently reviewed and ported into the actual C++ consensus code with functional tests. Founder/community/treasury allocations are intentionally not implemented; their mechanisms remain unresolved. Do not advertise S5 as live or send funds.
