#-------------------------------------------------------------------------------
#    Remove Duplactes from Sorted Array
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Completed 6/8/19
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Initialize pointer for insert.
3. Initalize counter.
4. Iterate through array moving the first integers found to the insert 
    pointer positions.
5. Truncate array when done. 
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def my_remove_duplicates(nums: [int]) -> int:
    """Remove extra duplicates from array and return new length."""
    insert_pt = 0
    last_seen = None

    for n in nums:
        if n != last_seen:
            last_seen = n
            nums[insert_pt] = n
            insert_pt += 1

    nums = nums[:insert_pt]
    return len(nums)

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        """Remove extra duplicates from array.

        Input:
        :nums: [int] -> sotrted list of integers
        
        Output:
        int -> length of updated array
        """
        return my_remove_duplicates(nums)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_1(self):
        nums = [1]
        ans = 1
        self.assertEqual(Solution().removeDuplicates(nums), ans)
    def test_11(self):
        nums = [1,1]
        ans = 1
        self.assertEqual(Solution().removeDuplicates(nums), ans)
    def test_111(self):
        nums = [1,1,1]
        ans = 1
        self.assertEqual(Solution().removeDuplicates(nums), ans)
    def test_ex1(self):
        nums = [1,1,2]
        ans = 2
        self.assertEqual(Solution().removeDuplicates(nums), ans)
    def test_ex2(self):
        nums = [0,0,1,1,1,2,2,3,3,4]
        ans = 5
        self.assertEqual(Solution().removeDuplicates(nums), ans)
        

unittest.main()
