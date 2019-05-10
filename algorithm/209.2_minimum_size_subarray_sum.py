# Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/
# Completed 4/28/19

class Solution:
    def minSubArrayLen(self, target: int, numbers: [int]) -> int:
        if sum(numbers) < target: return 0

        left, right = 0, 0
        subarray_sum = numbers[0]
        subarray_len = len(numbers)

        while left < len(numbers):
            if subarray_sum < target:
                if right == len(numbers) - 1: return subarray_len
                right += 1
                subarray_sum += numbers[right]
            else:
                subarray_len = min(subarray_len, right - left + 1)
                subarray_sum -= numbers[left]
                left += 1

        return subarray_len

#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_minSubArrayLen_pass(self):
        self.assertEqual(Solution().minSubArrayLen(7, [2,3,1,2,4,3]), 2)
    def test_minSubArrayLen_target_too_large(self):
        self.assertEqual(Solution().minSubArrayLen(200, [1,2,3,4,5]), 0)
    def test_minSubArrayLen_find_shortest_len(self):
        self.assertEqual(Solution().minSubArrayLen(3, [1, 1, 1, 3]), 1)

unittest.main()
