# Target Sum
# https://leetcode.com/problems/target-sum/
# Almost Completed 4/29/19
# Valid solution but times out for large inputs. 

class Solution:
    def findTargetSumWays(self, nums: [int], target: int, num_sum: int = 0, pointer: int = 0) -> int:
        if self.target_not_in_range(nums, target, num_sum, pointer):
            # Return 0 because this brance is not in range of the target
            return 0
        if pointer == len(nums) and num_sum == target:
            return 1

        return sum([
            self.findTargetSumWays(nums, target, num_sum + nums[pointer], pointer + 1),
            self.findTargetSumWays(nums, target, num_sum - nums[pointer], pointer + 1)
        ])
                
    def target_not_in_range(self, nums: [int], target: int, num_sum: int, pointer: int) -> bool:
        # Return True if the target is in the window of current sum +- remaining sum 
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
