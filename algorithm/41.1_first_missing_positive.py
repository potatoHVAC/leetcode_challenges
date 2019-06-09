#-------------------------------------------------------------------------------
#    First Missing Positive
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/first-missing-positive/
# Completed 6/8/19
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Convert list to set.
2. Count up from 1 checking if integer exists in set.
3. Return first integer that is not in set.
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def fmp(nums: [int]) -> int:
    """Return smallest missing positive integer in list."""
    nums_set = set(nums)
    for i in range(1, len(nums_set) + 2):
        if i not in nums:
            return i

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def firstMissingPositive(self, nums: [int]) -> int:
        """Return smallest missing positive integer in list.

        Input:
        :nums: [int] -> list of integers

        Output:
        int -> smallest integer not in :nums:
        """
        return fmp(nums)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_0(self):
        nums = [0]
        ans = 1
        self.assertEqual(Solution().firstMissingPositive(nums), ans)
    def test_1(self):
        nums = [1]
        ans = 2
        self.assertEqual(Solution().firstMissingPositive(nums), ans)
    def test_ex1(self):
        nums = [1,2,0]
        ans = 3
        self.assertEqual(Solution().firstMissingPositive(nums), ans)
    def test_ex2(self):
        nums = [3,4,-1,1]
        ans = 2
        self.assertEqual(Solution().firstMissingPositive(nums), ans)
    def test_ex3(self):
        nums = [7,8,9,11,12]
        ans = 1
        self.assertEqual(Solution().firstMissingPositive(nums), ans)

unittest.main()
