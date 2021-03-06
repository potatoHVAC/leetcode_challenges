# Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/
# Completed 4/28/19

"""Approach
1. Create dictionary that holds list elements as key and counts of those elements as values
2. Create list of all elements in the second list that were stored in the dictionary.
"""

class Solution:
    def intersection(self, nums1: [int], nums2: [int]) -> [int]:
        """Find all elements that exist in both input lists.

        Input:
        :nums1: [int] -- list of elements
        :nums2: [int] -- list of elements

        Output:
        [int] -- list of all ementes that exist in :nums1: and :nums2:
        """
        nums1_dict = self.count_elements_in(nums1)
        return self.compare_array_to_dict(nums2, nums1_dict)
        
    def count_elements_in(self, array: [int]) -> dict:
        """Create dictionary with elements as keys and element counts as values"""
        numbers = {}
        for num in array:
            if num in numbers: numbers[num] += 1
            else: numbers[num] = 1

        return numbers

    def compare_array_to_dict(self, array: [int], dictionary: dict) -> [int]:
        """Collect all elements from list that exist in dictionary"""
        intersect = []
        for num in array:
            if num in dictionary and num not in intersect:
                intersect.append(num)
        return list(intersect)

#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_count_elements_in_4_nums(self):
        array = [1, 2, 2, 4]
        answer = {1:1, 2:2, 4:1}
        self.assertEqual(Solution().count_elements_in(array), answer)
        
    def test_compare_array_to_dict_match_one(self):
        input_array = [1, 2]
        input_dict = {1:1, 3:3}
        answer = [1]
        self.assertEqual(Solution().compare_array_to_dict(input_array, input_dict), answer)
    def test_compare_array_to_dict_match_none(self):
        input_array = [1, 2]
        input_dict = {4:1, 3:3}
        answer = []
        self.assertEqual(Solution().compare_array_to_dict(input_array, input_dict), answer)
    def test_compare_array_to_dict_match_all(self):
        input_array = [1, 2]
        input_dict = {1:1, 2:1}
        answer = [1, 2]
        self.assertEqual(Solution().compare_array_to_dict(input_array, input_dict), answer)

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
        self.assertEqual(sorted(Solution().intersection(array1, array2)), answer)
        
unittest.main()
