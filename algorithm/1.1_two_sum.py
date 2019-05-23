#-------------------------------------------------------------------------------
#    Two Sum
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/two-sum/
# Completed 5/23/19
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Create list :memoize: with length 'target + 1'.
2. Scan :nums: and place index of each element into :memoize: at 'index == 
    element'
3. Check :memoize: index at 'target // 2' to catch matching cases 
    E.X. '2 + 2 == 4'
4. Scan :nums: and check for a value in :memoize: at 'index == target - element'
 4.1 If value is found then return that value and the current index sorted.
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

from collections import defaultdict

class TwoSum:
    def __init__(self, nums: [int], target: int):
        self.nums = nums
        self.target = target

    def scan_nums(self):
        memoize = defaultdict(list)
        for index, num in enumerate(self.nums):
            memoize[num].append(index)

        return memoize
    
    def _find_set(self, memoize):
        for index, num in enumerate(self.nums):
            difference = self.target - num
            if memoize[difference] and index != memoize[difference][0]:
                memoize[difference].append(index)
                return sorted(memoize[difference])

    def _sum_from_indecies(self, indecies):
        return sum([ self.nums[i] for i in indecies ])
        
    def solve(self) -> [int]:
        memoize = self.scan_nums()

        for indices in memoize.values():
            if len(indices) == 2 and self._sum_from_indecies(indices) == self.target:
                return sorted(indices)

        return self._find_set(memoize)
#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        return TwoSum(nums, target).solve()

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_1_2_3(self):
        nums = [1, 2]
        target = 3
        ans = [0,1]
        self.assertEqual(Solution().twoSum(nums, target), ans)
    def test_1_1_2(self):
        nums = [1, 1]
        target = 2
        ans = [0,1]
        self.assertEqual(Solution().twoSum(nums, target), ans)        
    def test_many(self):
        nums = [1, 2, 30, 4, 5, 6, 7, 8, 9]
        target = 36
        ans = [2,5]
        self.assertEqual(Solution().twoSum(nums, target), ans)        
    def test_0_1_1(self):
        nums = [0, 2, 1]
        target = 1
        ans = [0,2]
        self.assertEqual(Solution().twoSum(nums, target), ans)        
    def test_example1(self):
        nums = [2, 7, 11, 15]
        target = 9
        ans = [0,1]
        self.assertEqual(Solution().twoSum(nums, target), ans)
    def test_dont_duplicate_index(self):
        nums = [3, 2, 4]
        target = 6
        ans = [1, 2]
        self.assertEqual(Solution().twoSum(nums, target), ans)
    def test_negative(self):
        nums = [-1, -2, -3, -4, -5]
        target = -8
        ans = [2, 4]
        self.assertEqual(Solution().twoSum(nums, target), ans)
    def test_duplicate(self):
        nums = [1, 1, 2, 2, 3, 3, 7, 10]
        target = 17
        ans = [6, 7]
        self.assertEqual(Solution().twoSum(nums, target), ans)

unittest.main()
