#-------------------------------------------------------------------------------
#    Remove Duplicates From Sorted Array 2
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Completed 5/29/19
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Rrecord last seen number and the number of times it has been seen.
2. Track the insertion index for updates.
3. For the first one or two times a number is seen copy that number onto the 
    pointer location and increase the pointer.
4. Reset number and counter when new targets arrive.
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def remove_duplicates(nums: [int]) -> int:
    target = None
    count = 0
    pointer = 0

    for i in range(len(nums)):
        if target != nums[i]:
            target = nums[i]
            count = 1
            
        if count < 3:
            nums[pointer] = nums[i]
            count += 1
            pointer += 1

    nums = nums[:pointer]
    return pointer
    
#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        return remove_duplicates(nums)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_simple(self):
        arr = [1, 1, 1]
        ans = 2
        self.assertEqual(remove_duplicates(arr), ans)
    def test_double(self):
        arr = [1, 1, 2, 2]
        ans = 4
        self.assertEqual(remove_duplicates(arr), ans)
    def test_single(self):
        arr = [1]
        ans = 1
        self.assertEqual(remove_duplicates(arr), ans)
    def test_many(self):
        arr = [1, 1, 1, 2, 2, 2, 3, 3, 3]
        ans = 6
        self.assertEqual(remove_duplicates(arr), ans)
        
unittest.main()
