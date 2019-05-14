# Target Sum
# https://leetcode.com/problems/target-sum/
# Almost Completed 4/29/19
# Valid solution but times out for large inputs. 

"""Approach
1. Itterate through each list number
2. Add current number the previous sum
3. Subtrach current number from the previous sum (this path is a split form path 2)
4. Repeat 2 and 3 for each number
5. If the end sum == target then increment a counter
"""

class Solution:
    def findTargetSumWays(self, nums: [int], target: int, num_sum: int = 0, pointer: int = 0) -> int:
        """Find the number of ways to reach a value by either addint or subtracting each element of
        the input list.

        Input:
        :nums:    [int] -- list of integers to evaluate
        :target:  int   -- value that we want to reach
        :num_sum: int   -- running total for the current path
        :pointer: int   -- index of the number to evaluate

        Output:
        int -- number of ways to reach :target:
        """
        if self.target_not_in_range(nums, target, num_sum, pointer):
            return 0
        if pointer == len(nums) and num_sum == target:
            return 1

        add_current = self.findTargetSumWays(nums, target, num_sum + nums[pointer], pointer + 1)
        subtract_current = self.findTargetSumWays(nums, target, num_sum - nums[pointer], pointer + 1)
        return add_current + subtract_current
                
    def target_not_in_range(self, nums: [int], target: int, num_sum: int, pointer: int) -> bool:
        """Return True if the remaining numbers cannot move :num_sum: to :target:"""
        remaining_sum = sum(nums[pointer:])
        range_min = num_sum - remaining_sum
        range_max = num_sum + remaining_sum + 1
        return target not in range(range_min, range_max)

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
        
    def test_target_not_in_range_True(self):
        nums = [5, 1, 2]
        target = 5
        num_sum = 0
        pointer = 1
        self.assertTrue(Solution().target_not_in_range(nums, target, num_sum, pointer))
    def test_target_not_in_range_False(self):
        nums = [5, 1, 2]
        target = 5
        num_sum = 0
        pointer = 0
        self.assertFalse(Solution().target_not_in_range(nums, target, num_sum, pointer))

unittest.main()
