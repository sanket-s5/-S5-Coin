"""S5 reference helpers; not production consensus code."""
COIN = 100_000_000
MAX_MONEY = 21_000_000 * COIN
INITIAL_SUBSIDY = 30 * COIN
HALVING_INTERVAL = 210_000

def money_range(amount: int) -> bool:
    return isinstance(amount, int) and not isinstance(amount, bool) and 0 <= amount <= MAX_MONEY

def block_subsidy(height: int) -> int:
    if not isinstance(height, int) or isinstance(height, bool) or height < 0:
        raise ValueError("height must be a non-negative integer")
    halvings = height // HALVING_INTERVAL
    if halvings >= 64:
        return 0
    return INITIAL_SUBSIDY >> halvings

def scheduled_mining_issuance() -> int:
    total = 0
    for era in range(64):
        subsidy = INITIAL_SUBSIDY >> era
        if subsidy == 0:
            break
        total += subsidy * HALVING_INTERVAL
    return total
