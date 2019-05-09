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
        # Return the median of two lists.
        # Input lists must be sorted
        def _findMedianSortedArrays(
                nums_1: [int],
                lower_1: int,
                upper_1: int,
                nums_2: [int],
                lower_2: int,
                upper_2: int
        ) -> float:
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
        # Return the median of a sorted list.
        half_i = len(nums) // 2
        if len(nums)%2 == 0:
            return (nums[half_i - 1] + nums[half_i]) / 2
        else:
            return float(nums[half_i])

    def end_recursion(self, lower_1: int, upper_1: int, lower_2: int, upper_2: int) -> bool:
        # Return True if either list has been used up or if 2 or fewer numbers remain.
        if upper_1 <= lower_1 or upper_2 <= lower_2:
            return True
        elif abs(upper_1 - lower_1) + abs(upper_2 - lower_2) <= 2:
            return True
        return False

