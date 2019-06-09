#-------------------------------------------------------------------------------
#    Trapping Rain Water
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/trapping-rain-water/
# Completed 6/8/19
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Define function that turns array into stairs. 
 1.1 Traverse array keeping record of the largest number seen.
 1.2 If current number is smaller than largest then update to largest. 
2. Turn origional array in to a right handed stair. (small on left, large on 
    right)
3. Same for Left handed.
4. Traverse all three arrays taking the smaller of the stairs and comparing it 
    to the origional array. Add the difference to a sum.
5. return sum
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

class City:

    def __init__(self, height: [int]):
        self.height = height
        self.right_stairs = self._right_stair_gen()
        self.left_stairs = self._left_stair_gen()
        self.water_volume = 0
        self._solve()

    def _stair_gen(self, height: [int]) -> [int]:
        """Return list converted into stairs."""
        stairs = height.copy()
        for i in range(1,len(stairs)):
            stairs[i] = max(stairs[i], stairs[i - 1])
        return stairs
        
    def _right_stair_gen(self) -> [int]:
        """Return right handed stairs."""
        return self._stair_gen(self.height)

    def _left_stair_gen(self) -> [int]:
        """Return left handed stairs."""        
        return list(reversed(self._stair_gen(list(reversed(self.height)))))

    def _solve(self) -> 'self':
        """Find the volume of water trapped in the city."""
        for i in range(len(self.height)):
            water_lvl = min(self.right_stairs[i], self.left_stairs[i])
            self.water_volume += water_lvl - self.height[i]
        return self

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
        return City(height).water_volume

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
