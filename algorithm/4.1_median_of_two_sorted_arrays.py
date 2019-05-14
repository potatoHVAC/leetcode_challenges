# Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/
#

''' Approach
1 with 4 pointers reduce the lists from the outside in by comparing their elements.
2 Compare the first elements of each list and advance the pointer for the list with the smaller element.
3 Compare the last elemetns of each list and advance the pointer for the list with the larger element.
  * Only advance pointer if the upper and lower pointers are not equal.
4 Send to median algorithm if either list is used up or if 2 or less numbers remain.
5 Median algorithm will find the median of a single list by finding its center index(s).
'''

class Solution:
    def findMedianSortedArrays(self, nums_1: [int], nums_2: [int]) -> float:
        """Return the median value of two lists. The input lists must be sorted.

        Input:
        :nums_1: [int] -- sorted list of integers
        :nums_2: [int] -- sorted list of integers

        Output:
        float -- median of input lists
        """
        def _findMedianSortedArrays(
                nums_1: [int],
                lower_1: int,
                upper_1: int,
                nums_2: [int],
                lower_2: int,
                upper_2: int
        ) -> float:
            """Finds median by recursively removing elements from the ends of both lists"""
            if self.end_recursion(lower_1, upper_1, lower_2, upper_2):
                return self.median(nums_1[lower_1:upper_1] + nums_2[lower_2:upper_2])

            if nums_1[lower_1] < nums_2[lower_2]: lower_1 += 1
            else: lower_2 += 1

            if lower_1 == upper_1: upper_2 -= 1
            elif lower_2 == upper_2: upper_1 -= 1
            elif nums_1[upper_1 - 1] > nums_2[upper_2 - 1]: upper_1 -= 1
            else: upper_2 -= 1

            return _findMedianSortedArrays(nums_1, lower_1, upper_1, nums_2, lower_2, upper_2)
        return _findMedianSortedArrays(nums_1, 0, len(nums_1), nums_2, 0, len(nums_2))

    def median(self, nums: [int]) -> float:
        """Returns the median of a sorted list"""
        half_i = len(nums) // 2
        if len(nums)%2 == 0:
            return (nums[half_i - 1] + nums[half_i]) / 2
        else:
            return float(nums[half_i])

    def end_recursion(self, lower_1: int, upper_1: int, lower_2: int, upper_2: int) -> bool:
        """Check if the recursive function should exit.

        Output:
        True -- if either list is empty (right pointer is now lower than left)
        True -- if up to two elements remain between the two lists
        """
        if upper_1 <= lower_1 or upper_2 <= lower_2:
            return True
        elif abs(upper_1 - lower_1) + abs(upper_2 - lower_2) <= 2:
            return True
        return False

#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_findMedianSortedArrays_two_each_mixed(self):
        nums1 = [1, 3]
        nums2 = [2, 4]
        answer = 2.5
        self.assertEqual(Solution().findMedianSortedArrays(nums1, nums2), answer)
    def test_findMedianSortedArrays_two_each_middle(self):
        nums1 = [1, 3]
        nums2 = [2, 2]
        answer = 2.0
        self.assertEqual(Solution().findMedianSortedArrays(nums1, nums2), answer)
    def test_findMedianSortedArrays_two_each_small_large(self):
        nums1 = [1, 3]
        nums2 = [5, 6]
        answer = 4.0
        self.assertEqual(Solution().findMedianSortedArrays(nums1, nums2), answer)
    def test_findMedianSortedArrays_one_each(self):
        nums1 = [1]
        nums2 = [2]
        answer = 1.5
        self.assertEqual(Solution().findMedianSortedArrays(nums1, nums2), answer)
    def test_findMedianSortedArrays_one_large_one_small(self):
        nums1 = [1]
        nums2 = [2, 3, 4, 5, 6]
        answer = 3.5
        self.assertEqual(Solution().findMedianSortedArrays(nums1, nums2), answer)
    def test_findMedianSortedArrays_two_large(self):
        nums1 = [1, 2, 3, 4]
        nums2 = [5, 6, 7, 8]
        answer = 4.5
        self.assertEqual(Solution().findMedianSortedArrays(nums1, nums2), answer)
    def test_findMedianSortedArrays_one_in_middle(self):
        nums1 = [5]
        nums2 = [1, 2, 8, 9]
        answer = 5.0
        self.assertEqual(Solution().findMedianSortedArrays(nums1, nums2), answer)

    def test_median_even_length(self):
        self.assertEqual(Solution().median([1, 2]), 1.5)
    def test_median_odd_length(self):
        self.assertEqual(Solution().median([1, 2, 3]), 2.0)
    def test_median_length_1(self):
        self.assertEqual(Solution().median([1]), 1.0)

    def test_end_recursion_false(self):
        self.assertFalse(Solution().end_recursion(1,4,1,4))
    def test_end_recursion_empty_lower(self):
        self.assertTrue(Solution().end_recursion(1,1,1,4))
    def test_end_recursion_empty_upper(self):
        self.assertTrue(Solution().end_recursion(1,4,1,1))
    def test_end_recursion_two_left(self):
        self.assertTrue(Solution().end_recursion(1,2,1,2))

unittest.main()
