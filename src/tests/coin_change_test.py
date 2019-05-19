from unittest import TestCase
from coin_change import CoinChange


class TestCoinChange(TestCase):
    def test_coin_should_be_5(self):
        coin = CoinChange(4, 28, [10, 5, 2, 1])
        result = len(coin.get_smallest_coin())
        self.assertEqual(result, 5)

    def test_coin_should_be_3(self):
        coin = CoinChange(3, 13, [5, 4, 1])
        result = len(coin.get_smallest_coin())
        self.assertEqual(result, 3)

    def test_coin_should_be_2(self):
        coin = CoinChange(3, 8, [5, 4, 1])
        result = len(coin.get_smallest_coin())
        self.assertEqual(result, 2)
