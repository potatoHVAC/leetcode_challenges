# Target Sum
# https://leetcode.com/problems/target-sum/
# Completed 4/30/19

"""Approach
1. Use dynamic programming.
2. Create a dictionary with integers as keys and the number of ways to sum to
   that integer as the values. Initial state is {0:1} because there is 1 way
   to get to 0 before inserting numbers. 
3. Itterate over each number inserting them to a new dictionary.
  3.1 Find every element of the old dictionary and insert the value of its keys 
      to thew new dictionary under the key added to the new number.
  3.2 Repeat the previous step with subtracting the new number form the key. 
  3.3 Replace the counter old dictionary with the new couter dictionary.
4. Return the number of ways to reach the target sum.
"""

from collections import defaultdict

class Solution:
    def __init__(self):
        self.counts = defaultdict(int)
        self.counts[0] += 1
    
    def ingest_numbers(self, numbers: [int]):
        """Use the new number to calculate all new possible paths and the number
        of ways to get there
        """
        for number in numbers:
            self.update_sum_counter(number)
        return self

    def update_sum_counter(self, number: int):
        """Create counter dictionary that holds all possible paths and the number of
        ways to get there. Then replace the old self.counts with the new dictionary.
        """
        new_counts = defaultdict(int)
        for num_key, count in self.counts.items():
            new_counts[num_key + number] += count
            new_counts[num_key - number] += count
            
        self.counts = new_counts
        return self

    def get_target_count(self, target: int) -> int:
        """Return the number of ways to sum to the target integer"""
        return self.counts[target]

    def findTargetSumWays(self, numbers: [int], target: int) -> int:
        """Return the nuber of ways to sum to the target integer

        Input:
        :numbers: [int] -- list of integers to sum
        :target:  int   -- value to count the ways to sum

        Output:
        int -- number of ways to sum to :target:
        """
        return self.ingest_numbers(numbers).get_target_count(target)

#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_findTargetSumWays_1(self):
        nums = [1]
        target = 1
        answer = 1
        self.assertEqual(Solution().findTargetSumWays(nums, target), answer)
    def test_findTargetSumWays_1_negative(self):
        nums = [1]
        target = -1
        answer = 1
        self.assertEqual(Solution().findTargetSumWays(nums, target), answer)
    def test_findTargetSumWays_2(self):
        nums = [1, 1]
        target = 0
        answer = 2
        self.assertEqual(Solution().findTargetSumWays(nums, target), answer)
    def test_findTargetSumWays_3(self):
        nums = [1, 1, 1, 1, 1]
        target = 3
        answer = 5
        self.assertEqual(Solution().findTargetSumWays(nums, target), answer)
    def test_findTargetSumWays_4(self):
        nums = [1, 2, 3]
        target = 0
        answer = 2
        self.assertEqual(Solution().findTargetSumWays(nums, target), answer)

unittest.main()
