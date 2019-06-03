#-------------------------------------------------------------------------------
#    Triangle
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/triangle/
# Completed 6/3/19
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Dynamic Programming
 1.1 If node is bottom of the triangle, return node
 1.2 Find next left node and next right node
 1.3 Add current node + min(left, right)
 1.4 Memoize node
 1.5 return memoize[node]
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

class Triangle:

    def __init__(self, triangle):
        self.triangle = triangle

    def solve(self) -> int:
        """Return the sum of the minimum path"""

        if len(self.triangle) == 0:
            return 0

        memoize = {}
        def _solve(i: int, j: int) -> int:
            triangle_key = (i,j)

            if triangle_key not in memoize:
                if i == len(self.triangle) - 1:
                    memoize[triangle_key] = self.triangle[i][j]
                else:
                    left_path = _solve(i + 1, j)
                    right_path = _solve(i + 1, j + 1)
                    min_path = min(left_path, right_path)
                    memoize[triangle_key] = self.triangle[i][j] + min_path

            return memoize[triangle_key]

        return _solve(0, 0)

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def minimumTotal(self, triangle: [[int]]) -> int:
        """Return the sum of the minimum path

        Input: 
        :triangle: [[int]] -> triangle list of integer lists
        
        Output:
        int -> total sum of the minimum path
        """
        return Triangle(triangle).solve()

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_empty(self):
        triangle = []
        ans = 0
        self.assertEqual(Solution().minimumTotal(triangle), ans)
    def test_1lvl(self):
        triangle = [[1]]
        ans = 1
        self.assertEqual(Solution().minimumTotal(triangle), ans)
    def test_2lvl(self):
        triangle = [
            [1],
            [2,3]
        ]
        ans = 3
        self.assertEqual(Solution().minimumTotal(triangle), ans)        
    def test_neg(self):
        triangle = [
            [1],
            [-2,-3]
        ]
        ans = -2
        self.assertEqual(Solution().minimumTotal(triangle), ans)
    def test_neg(self):
        triangle = [
            [1],
            [2,1],
            [5,1,3],
            [2,2,1,5],
            [4,3,1,5,7]
        ]
        ans = 5
        self.assertEqual(Solution().minimumTotal(triangle), ans)
    def test_ones(self):
        triangle = [
            [1],
            [1] * 2,
            [1] * 3,
            [1] * 4,
            [1] * 5,            
            [1] * 6,
            [1] * 7,
            [1] * 8,
            [1] * 9,
            [1] * 10            
        ]
        ans = 10
        self.assertEqual(Solution().minimumTotal(triangle), ans)

        
unittest.main()
