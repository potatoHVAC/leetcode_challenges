# Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/
# Completed 4/28/19

class Solution:
    def intersection(self, nums1: [int], nums2: [int]) -> [int]:
        return list(set(nums1) & set(nums2))
        
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):
    
    def test_intersection_match_none(self):
        array1 = [1, 2]
        array2 = [3, 4]
        answer = []
        self.assertEqual(Solution().intersection(array1, array2), answer)
    def test_intersection_match_one(self):
        array1 = [1, 2]
        array2 = [2, 4]
        answer = [2]
        self.assertEqual(Solution().intersection(array1, array2), answer)
    def test_intersection_match_all(self):
        array1 = [1, 2]
        array2 = [1, 2]
        answer = [1, 2]
        self.assertEqual(Solution().intersection(array1, array2), answer)
    def test_intersection_match_many(self):
        array1 = [1, 2, 3, 6, 3, 2, 1, 3, 5]
        array2 = [3, 4, 7, 3, 2, 5]
        answer = [2, 3, 5]
        self.assertEqual(Solution().intersection(array1, array2), answer)
        
unittest.main()
