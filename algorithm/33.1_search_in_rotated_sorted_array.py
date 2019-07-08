#-------------------------------------------------------------------------------
#    Search in Rotated Sorted Array
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Completed 7/8/19
#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def rotated_pivot_num(nums: [int], target: int, pointer: int):
    """Return a modified value for nums[pointer] depending on the pointer's 
    relationship to :target:
    """
    if target >= nums[0] and nums[pointer] < nums[0]:
        return float("inf")
    elif target < nums[0] and nums[pointer] >= nums[0]:
        return float("-inf")
    return nums[pointer]

def rotated_binary_search(nums: [int], target: int) -> int:
    """Return the index of :target: in :nums: or -1 if not in list
    
    :type nums: [int] -> sorted list of integers that is rotated about one point
    :type target: int -> number to find in list
    :rtype: int -> position of :target:
    """
    def _rotated_binary_search(nums: [int], target: int, left: int, right: int):
        if left > right:
            return -1

        mid = left + (right - left) // 2
        pivot_num = rotated_pivot_num(nums, target, mid)
        if pivot_num == target:
            return mid
        elif pivot_num < target:
            return _rotated_binary_search(nums, target, mid+1, right)
        return _rotated_binary_search(nums, target, left, mid-1)

    return _rotated_binary_search(nums, target, 0, len(nums)-1)
    

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def search(self, nums: [int], target: int) -> int:
        return rotated_binary_search(nums, target)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_1(self):
        target = 8
        nums = [6,7,8,9,1,2,3,4,5]
        ans = 2
        self.assertEqual(ans, Solution().search(nums, target))
    def test_2(self):
        target = 1
        nums = [1,0]
        ans = 0
        self.assertEqual(ans, Solution().search(nums, target))
    def test_3(self):
        target = 0
        nums = [0]
        ans = 0
        self.assertEqual(ans, Solution().search(nums, target))
    def test_4(self):
        target = 1
        nums = [0]
        ans = -1
        self.assertEqual(ans, Solution().search(nums, target))
    def test_5(self):
        target = 0
        nums = [3,4,5]
        ans = -1
        self.assertEqual(ans, Solution().search(nums, target))
    def test_6(self):
        target = 99
        nums = [x for x in range(100)]
        ans = 99
        self.assertEqual(ans, Solution().search(nums, target))
    def test_7(self):
        target = 0
        nums = [1]
        ans = -1
        self.assertEqual(ans, Solution().search(nums, target))
    def test_8(self):
        target = 4
        nums = [6,7,8,9,1,2,3,4,5]
        ans = 7
        self.assertEqual(ans, Solution().search(nums, target))
    def test_9(self):
        target = 4
        nums = [6,7,8,9,10,11,12,4]
        ans = 7
        self.assertEqual(ans, Solution().search(nums, target))
    def test_10(self):
        target = 44
        nums = [44,1,2,3,4,5,6,7,8]
        ans = 0
        self.assertEqual(ans, Solution().search(nums, target))
    def test_11(self):
        target = 3
        nums = [4,5,6,7,0,1,2]
        ans = -1
        self.assertEqual(ans, Solution().search(nums, target))

unittest.main()
