#-------------------------------------------------------------------------------
#    Climbing Stairs
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/climbing-stairs/
# Completed 6/13/19
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Dynamic Solution
2. Memoize starts at 0=1 and 1=1
3. Return ans = f(n-1) f(n-2)
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

class Stairs:

    def __init__(self):
        self.memoize = {0: 1, 1: 1}

    def ways_to(self, n: int) -> int:
        """Return the number of ways to climb to :n:"""
        if n not in self.memoize:
            self.memoize[n] = self.ways_to(n-1) + self.ways_to(n-2)
        return self.memoize[n]

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def climbStairs(self, n: int) -> int:
        """Return the number of ways to climb to :n:

        Input:
        :n: int -> target stair height

        Output:
        int -> number of ways to get to :n:
        """        
        return Stairs().ways_to(n)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_1(self):
        n = 1
        ans = 1
        self.assertEqual(Solution().climbStairs(n), ans)
    def test_2(self):
        n = 2
        ans = 2
        self.assertEqual(Solution().climbStairs(n), ans)
    def test_2(self):
        n = 2
        ans = 2
        self.assertEqual(Solution().climbStairs(n), ans)
    def test_3(self):
        n = 3
        ans = 3
        self.assertEqual(Solution().climbStairs(n), ans)
    def test_4(self):
        n = 4
        ans = 5
        self.assertEqual(Solution().climbStairs(n), ans)
    def test_20(self):
        n = 20
        ans = 10946
        self.assertEqual(Solution().climbStairs(n), ans)

unittest.main()
