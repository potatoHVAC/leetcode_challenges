#-------------------------------------------------------------------------------
#    Best Time to Buy and Sell Stock
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Completed 6/13/19
#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def max_profit(prices: [int]) -> int:
    """Return maximum profit for 1 buy 1 sell given a list of prices."""
    max_profit_found = 0
    previous_price = float('inf')
    previous_low_price = float('inf')

    for price in prices:
        max_profit_found = max(price - previous_low_price, max_profit_found)
        previous_price = price
        previous_low_price = min(price, previous_low_price)

    return max_profit_found

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def maxProfit(self, prices: [int]) -> int:
        """Return maximum profit for 1 buy 1 sell given a list of prices.
        
        Input:
        prices: [int] -> chronological list of stock prices 

        Output:
        int -> max profit for 1 buy 1 sell
        """
        return max_profit(prices)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_none(self):
        prices = [2,1]
        ans = 0
        self.assertEqual(Solution().maxProfit(prices), ans)
    def test_easy(self):
        prices = [1,2]
        ans = 1
        self.assertEqual(Solution().maxProfit(prices), ans)
    def test_find_second_range(self):
        prices = [2,5,1,20]
        ans = 19
        self.assertEqual(Solution().maxProfit(prices), ans)
    def test_ex1(self):
        prices = [7,1,5,3,6,4]
        ans = 5
        self.assertEqual(Solution().maxProfit(prices), ans)
    def test_ex2(self):
        prices = [7,6,4,3,1]
        ans = 0
        self.assertEqual(Solution().maxProfit(prices), ans)

unittest.main()
