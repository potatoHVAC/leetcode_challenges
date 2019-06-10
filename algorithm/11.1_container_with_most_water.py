#-------------------------------------------------------------------------------
#    Container With Most Water
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/container-with-most-water/
# Completed 6/9/19
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Two pointer.
2. Initialize max fcontainer found. 
3. Starting With left and right pointers.
 3.1 Find volume between pointers. 
 3.2 Update max found.
 3.3 Incriment the smaller of the two pointers. 
 3.4 If matching sizes. Split for both paths.
     Note, use dynamic to prevent duplicate recursion.
4. Return max found.
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def max_area(height: [int]) -> int:
    """Return largest volume contained by two heights."""

    memoize = set()
    def _max_area(left: int, right: int):
        if left >= right or (left, right) in memoize:
            return 0
        
        memoize.add((left, right))
        volume = min(height[left], height[right]) * (right - left)
        
        left_v = right_v = 0
        if height[left] >= height[right]:
            volume = max(volume, _max_area(left, right - 1))
        if height[left] <= height[right]:
            volume = max(volume, _max_area(left + 1, right))
        return volume

    return _max_area(0, len(height) - 1)

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def maxArea(self, height: [int]) -> int:
        """Return largets volume contained by two heights.

        Input:
        :height: [int] -> list of wall heights

        Output:
        int -> max volume found
        """
        return max_area(height)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_11(self):
        height = [1,1]
        ans = 1
        self.assertEqual(Solution().maxArea(height), ans)
    def test_101(self):
        height = [10,0,10]
        ans = 20
        self.assertEqual(Solution().maxArea(height), ans)
    def test_000(self):
        height = [0,0,0]
        ans = 0
        self.assertEqual(Solution().maxArea(height), ans)
    def test_empty(self):
        height = []
        ans = 0
        self.assertEqual(Solution().maxArea(height), ans)
    def test_1(self):
        height = [5]
        ans = 0
        self.assertEqual(Solution().maxArea(height), ans)
    def test_ex1(self):
        height = [1,8,6,2,5,4,8,3,7]
        ans = 49
        self.assertEqual(Solution().maxArea(height), ans)

unittest.main()
