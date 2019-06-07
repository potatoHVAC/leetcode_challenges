#-------------------------------------------------------------------------------
#    Jump Game II
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/jump-game-ii/
# Completed 6/7/19
#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def jump_game(nums):
    """Return fewest number of jumps to last position."""
    jumps = 0
    total_distance = 0
    max_distance = 0

    for i in range(len(nums)):
        if i > total_distance:
            total_distance = max_distance
            jumps += 1
            
        max_distance = max(max_distance, i + nums[i])
        
    return jumps

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def jump(self, nums: [int]) -> int:
        """Return fewest number of jumps to last position.
        
        Input:
        :nums: [int] -> list of jump ranges

        Output:
        int -> number of jumps taken
        """
        return jump_game(nums)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_1(self):
        nums = [1]
        ans = 0
        self.assertEqual(Solution().jump(nums), ans)
    def test_1s(self):
        nums = [1,1,1,1,1,1,1,1,1,1]
        ans = 9
        self.assertEqual(Solution().jump(nums), ans)
    def test_ex1(self):
        nums = [2,3,1,1,4]
        ans = 2
        self.assertEqual(Solution().jump(nums), ans)
    def test_overshoot(self):
        nums = [5,1]
        ans = 1
        self.assertEqual(Solution().jump(nums), ans)
    def test_zeros(self):
        nums = [5,0,0,0,0,1]
        ans = 1
        self.assertEqual(Solution().jump(nums), ans)

unittest.main()
