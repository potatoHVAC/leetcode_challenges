# Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/
# Almost completed 4/27/19
# Fails with large inputs due to recursive depth size

class Solution:
    def minSubArrayLen(self, target: int, numbers: [int]) -> int:
        """Find lenght of minimum sub array with the sum less than a target integer.

        Input:
        :target:  int   -- sub array's sum must be less than :target:
        :numbers: [int] -- list of integers to find sub array

        Output:
        int -- length of shortest sub array in :numbers: with sum less than :target:
        """
        if sum(numbers) < target: return 0
    
        def _min_sub_array_len(target, numbers, min_len = len(numbers), left: int = 0, right: int = 0) -> int:
            """Find length of minimum sub array."""
            if right > len(numbers): return min_len
            
            if sum(numbers[left:right]) < target:
                return _min_sub_array_len(target, numbers, min_len, left, right + 1)
            else:
                new_min_len = min([min_len, right - left])
                return _min_sub_array_len(target, numbers, new_min_len, left + 1, right)

        return _min_sub_array_len(target, numbers)

    
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
