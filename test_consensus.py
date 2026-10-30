import unittest
from s5.consensus import COIN, MAX_MONEY, HALVING_INTERVAL, money_range, block_subsidy, scheduled_mining_issuance

class S5ReferenceTests(unittest.TestCase):
    def test_initial_reward(self):
        self.assertEqual(block_subsidy(0), 30 * COIN)
    def test_halving_boundary(self):
        self.assertEqual(block_subsidy(HALVING_INTERVAL - 1), 30 * COIN)
        self.assertEqual(block_subsidy(HALVING_INTERVAL), 15 * COIN)
    def test_second_halving(self):
        self.assertEqual(block_subsidy(2 * HALVING_INTERVAL), 750_000_000)
    def test_zero_reward(self):
        self.assertEqual(block_subsidy(32 * HALVING_INTERVAL), 0)
    def test_negative_height(self):
        with self.assertRaises(ValueError):
            block_subsidy(-1)
    def test_money_range(self):
        self.assertTrue(money_range(0))
        self.assertTrue(money_range(MAX_MONEY))
        self.assertFalse(money_range(-1))
        self.assertFalse(money_range(MAX_MONEY + 1))
        self.assertFalse(money_range(1.5))
        self.assertFalse(money_range(True))
    def test_total_scheduled_issuance(self):
        self.assertEqual(scheduled_mining_issuance(), 1_259_999_997_480_000)

if __name__ == "__main__":
    unittest.main()
