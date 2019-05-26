#-------------------------------------------------------------------------------
#    Cherry Pickup
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/cherry-pickup/
# Almost Complete 5/26/19
# Times out for large inputs
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. DFS 
2. Check if current tile is cherry or wall
 2.1 Return path if last found and bottom left tile was touched
 2.2 If wall or out of bounds, return empty path
 2.3 Find max of two future paths ([lef, down] for going in and [up, right] for 
      returning).
 2.4 If cherry, add to max future path and return path.
3. Return length of path
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

from collections import defaultdict

class Tile:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.up = None
        self.down = None

class Board:
    def __init__(self, mat: [[int]]):
        self.board = mat
        self._build_board(mat)._set_relationships()

    def _build_board(self, mat: [[int]]) -> 'self':
        """Create tiles from mat"""
        for row in range(0, len(mat)):
            for col in range(0, len(mat[0])):
                self.board[row][col] = Tile(mat[row][col])
        return self

    def _set_relationships(self):
        """Populate all tile relationships [left, right, up, down]"""
        for row in range(0, len(self.board)):
            for col in range(0, len(self.board[0])):
                tile = self.board[row][col]

                if row > 0:
                    tile.up = self.board[row - 1][col]
                if row < len(self.board) - 1:
                    tile.down = self.board[row + 1][col]
                if col > 0:
                    tile.left = self.board[row][col - 1]
                if col < len(self.board[0]) - 1:
                    tile.right = self.board[row][col + 1]

    def _found_last(self, tile: Tile) -> bool:
        """Return true if input :tile: is the bottom right tile"""
        row = len(self.board) - 1
        col = len(self.board[0]) - 1
        return tile == self.board[row][col]
                    
    def solve(self):
        """Find the maximum number of cherries that can be picked"""
        
        def _max(arr1: [Tile], arr2: [Tile]) -> [Tile]:
            """Return the maximum length list of Tiles"""
            if len(arr1) > len(arr2):
                return arr1
            return arr2
        
        def _solve(tile: Tile, count: set, go_back: bool) -> [Tile]:
            if tile is None or tile.val == -1:
                return []
                
            if self._found_last(tile):
                go_back = True
            if tile.val == 1:
                count.add(tile)
            if go_back and tile == self.board[0][0]:
                return count

            elif go_back:
                left = _solve(tile.left, count.copy(), True)
                up = _solve(tile.up, count.copy(), True)
                return _max(left, up)
            else:
                down = _solve(tile.down, count.copy(), False)
                right = _solve(tile.right, count.copy(), False)
                return _max(down, right)
                    
        return len(_solve(self.board[0][0], set(), False))

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def cherryPickup(self, grid: [[int]]) -> int:    
        """Main function for solving Leetcode Input

        Input:
        :mat: [[int]] -> 2D array of integers
        
        Output:
        int -> maximum number of picked cherrys 
        """
        return Board(grid).solve()

#-------------------------------------------------------------------------------
#   Test
#-------------------------------------------------------------------------------

import unittest

class TestBoard(unittest.TestCase):

    def test_simple(self):
        mat = [
            [ 0, 1],
            [-1, 0]
        ]
        self.assertEqual(Board(mat).solve(), 1)
    def test_dont_double_count_path(self):
        mat = [
            [ 1, 1],
            [-1, 1]
        ]
        self.assertEqual(Board(mat).solve(), 3)
    def test_all_walls_except_start(self):
        mat = [
            [ 1,-1],
            [-1,-1]
        ]
        self.assertEqual(Board(mat).solve(), 0)
    def test_single_1(self):
        mat = [[1]]
        self.assertEqual(Board(mat).solve(), 1)
    def test_single_wall(self):
        mat = [[-1]]
        self.assertEqual(Board(mat).solve(), 0)
    def test_single_0(self):
        mat = [[0]]
        self.assertEqual(Board(mat).solve(), 0)           
    def test_start_is_wall(self):
        mat = [
            [-1, 1],
            [ 1, 1]
        ]
        self.assertEqual(Board(mat).solve(), 0)
        
    def test_end_is_wall(self):
        mat = [
            [ 1, 0],
            [ 0,-1]
        ]
        self.assertEqual(Board(mat).solve(), 0)
    def test_empty_rectangle(self):
        mat = [
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(Board(mat).solve(), 0)
    def test_multiple_paths(self):
        mat = [
            [ 0, 0, 0, 0, 0],
            [ 1,-1, 1,-1, 1],
            [ 0, 0, 0, 0, 0]
        ]
        self.assertEqual(Board(mat).solve(), 2)
    def test_sparse(self):
        mat = [
            [ 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0],            
            [ 0, 0, 1, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0],
            [ 1, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(Board(mat).solve(), 2)
    def test_barrior(self):
        mat = [
            [ 1, 1, 1, 1,-1, 1],
            [ 1, 1, 1,-1, 1, 1],            
            [ 1, 1,-1, 1, 1, 1],
            [ 1,-1, 1, 1, 1, 1],
            [-1, 1, 1, 1, 1, 1]
        ]
        self.assertEqual(Board(mat).solve(), 0)
    def test_find_max_path1(self):
        mat = [
            [ 0, 0, 0, 1, 1, 1],
            [ 1,-1, 1, 0, 0, 0],
            [ 1,-1,-1,-1,-1, 0],
            [ 1, 1, 1, 1, 1, 0]
        ]
             
        self.assertEqual(Board(mat).solve(), 10)
    def test_find_max_path_2(self):
        mat = [
            [ 0, 0, 0, 0, 0, 1],
            [ 0,-1, 1, 0, 0, 0],            
            [ 1,-1, 1, 0, 0, 0],
            [ 1,-1,-1,-1,-1, 0],
            [ 1, 1, 1, 1, 1, 0]
        ]
        self.assertEqual(Board(mat).solve(), 9)            
    def test_find_max_path3(self):
        mat = [
            [ 0, 1, 0, 1, 1, 1],
            [ 0,-1, 0, 0, 0, 0],            
            [ 0,-1, 1, 1, 1, 0],
            [ 0,-1,-1,-1,-1, 1],
            [ 1, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(Board(mat).solve(), 8)
    def test_find_max_path4(self):
        mat = [
            [ 0, 1, 0, 1, 1, 1],
            [ 0,-1, 0, 0, 0, 0],            
            [ 0,-1, 1, 1, 1, 0],
            [ 0,-1,-1,-1,-1, 1],
            [ 1, 1, 0, 0, 0, 0]
        ]
        self.assertEqual(Board(mat).solve(), 8)
    def test_find_max_path5(self):
        mat = [
            [ 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 1, 1],            
            [ 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 1, 1]
        ]
        self.assertEqual(Board(mat).solve(), 18)
    def test_find_max_path6(self):
        mat = [
            [ 1, 1, 1, 1,-1, 1],
            [ 1, 1, 1,-1, 1, 1],            
            [ 1, 1, 1, 1, 1, 1],
            [ 1,-1, 1, 1, 1, 1],
            [-1, 1, 1, 1, 1, 1]
        ]
        self.assertEqual(Board(mat).solve(), 17)
    def test_find_max_path7(self):
        mat = [
            [ 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1,-1, 1, 1],            
            [ 1, 1, 1, 1, 1, 1],
            [ 1,-1, 1, 1, 1, 1],
            [-1, 1, 1, 1, 1, 1]
        ]
        self.assertEqual(Board(mat).solve(), 18)
    def test_find_max_path8(self):
        mat = [
            [ 1, 1, 0, 1],
            [ 1,-1, 1, 0],            
            [ 0,-1,-1, 0],
            [ 0, 1,-1, 1],
            [ 1, 0, 1, 1]
        ]
        self.assertEqual(Board(mat).solve(),  8)
    def test_find_max_path9(self):
        mat = [
            [ 1, 1, 1, 1, 0, 0, 0],
            [ 0, 0, 0, 1, 0, 0, 0],
            [ 0, 0, 0, 1, 0, 0, 1],
            [ 1, 0, 0, 1, 0, 0, 0],
            [ 0, 0, 0, 1, 0, 0, 0],
            [ 0, 0, 0, 1, 0, 0, 0],
            [ 0, 0, 0, 1, 1, 1, 1]
        ]
        self.assertEqual(Board(mat).solve(), 15)
    def test_find_dont_get_destracted(self):
        mat = [
            [ 0, 0, 0, 0, 0, 0, 0],
            [-1,-1,-1,-1,-1,-1, 0],
            [ 1, 1, 1, 1, 1, 1, 0],
            [ 1, 1, 1, 1, 1, 1, 0],
            [ 1, 1, 1, 1, 1, 1, 0],
            [ 1, 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 1, 1, 1]
        ]
        self.assertEqual(Board(mat).solve(), 2)        

unittest.main()
    
