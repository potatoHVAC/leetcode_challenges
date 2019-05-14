# Coin Change 2
# https://leetcode.com/problems/coin-change-2/
# Completed 4/26/19

class Coin:
    def __init__(self, value: int):
        self.value = value

class Currency:
    def __init__(self, coins: [int]):
        self.coins = [ Coin(coin) for coin in coins ]

    def change_permutations(self, target: int) -> int:
        """Return the number of ways to make change with the given currency"""
        counting_up = [1] + [ 0 for _ in range(target) ]
        for coin in self.coins:
            for i in range(target + 1):
                next_sum = i + coin.value
                
                if next_sum <= target:
                    counting_up[next_sum] += counting_up[i]

        return counting_up[target]

class Solution:
    def change(self, target: int, coins: [int]) -> int:
        """Return the number of ways to make change with the given currency.

        Input:
        :target: int   -- target value to count the number of ways to make change
        :coins:  [int] -- list of integers representing the different coin values

        Output:
        int -- number of ways to make change
        """
        return Currency(coins).change_permutations(target)

#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_change_simple(self):
        self.assertEqual(Solution().change(1, [1]), 1)
    def test_change_zero(self):
        self.assertEqual(Solution().change(1, [2]), 0)
    def test_change_two(self):
        self.assertEqual(Solution().change(3, [1,2]), 2)
    def test_change_5_125(self):
        self.assertEqual(Solution().change(5, [1,2,5]), 4)

unittest.main()
