#-------------------------------------------------------------------------------
#    Trapping Rain Water
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/trapping-rain-water/
# Completed 6/8/19
# I wanted to attempt this with two pointers
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Two pointer method
2. Traverse from left and right at same time.
3. Keep record of previous max height for each pointer.
4. If left element < right element.
 4.1 Update left max if needed.
 4.2 Add water difference.
 4.3 Update left pointer.
5. Else do sep 4 for right.
6. Return volume of water when left > right.
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def drown(height: [int]) -> int:
    """Return the volume of water trapped in the city."""

    def _drown(lp: int, rp: int, l_lvl: int, r_lvl: int, water: int) -> int:
        if lp > rp:
            return water
        elif height[lp] < height[rp]:
            l_lvl = max(l_lvl, height[lp])
            water += l_lvl - height[lp]
            lp += 1
        else:
            r_lvl = max(r_lvl, height[rp])
            water += r_lvl - height[rp]
            rp -= 1
        return _drown(lp, rp, l_lvl, r_lvl, water)

    return _drown(0, len(height) - 1, 0, 0, 0)


#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def trap(self, height: [int]) -> int:
        """Return the volume of water trapped in the city.

        Input:
        :height: [int] -> list of elevation integers

        Output:
        int -> volume of trapped water
        """
        return drown(height)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_1(self):
        city = [1]
        ans = 0
        self.assertEqual(Solution().trap(city), ans)
    def test_121(self):
        city = [1,2,1]
        ans = 0
        self.assertEqual(Solution().trap(city), ans)
    def test_102(self):
        city = [1,0,2]
        ans = 1
        self.assertEqual(Solution().trap(city), ans)
    def test_ex1(self):
        city = [0,1,0,2,1,0,1,3,2,1,2,1]
        ans = 6
        self.assertEqual(Solution().trap(city), ans)

        
unittest.main()
