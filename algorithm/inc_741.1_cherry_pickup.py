#-------------------------------------------------------------------------------
#   Cherry Picking
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://github.com/potatoHVAC/leetcode_challenges/tree/master/algorithm
# Not Complete

from collections import defaultdict

class Tile:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.up = None
        self.down = None

class Board:
    def __init__(self, mat):
        self.board = [ row.copy() for row in mat ]
        self.build_board(mat).set_relationships()

    def to_s(self) -> str:
        """Format board to string"""
        def _to_str(tile):
            if tile.val == -1:
                return str(-1)
            return " " + str(tile.val)
        
        return "\n".join([
            ",".join(list(map(_to_str, row))) for row in self.board
        ])

    def to_sx(self, path) -> str:
        def _to_str(tile):
            if tile.val == -1:
                output = str(-1)
            else:
                output = " " + str(tile.val)
            if tile in path:
                output = output[0] + 'x'
            return output
        
        return "\n".join([
            ",".join(list(map(_to_str, row))) for row in self.board
        ])    

    def build_board(self, mat) -> 'self':
        """Populate board tiles with values

        Input:
        :mat: [[int]] -> 2D array of integers
        """
        for row in range(0, len(mat)):
            for col in range(0, len(mat[0])):
                self.board[row][col] = Tile(mat[row][col])
        return self

    def set_relationships(self):
        """Populate tile relationships"""
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

    def last_tile(self) -> Tile:
        """Return last tile object"""
        row = len(self.board) - 1
        col = len(self.board[0]) - 1
        return self.board[row][col]
    
    def found_last(self, tile: Tile) -> bool:
        """Return True if tile is the end of the mine"""
        return tile == self.last_tile()

    def solve(self) -> int:

        def _setup_memoize(memoize) -> dict:
            memoize[None] = set()
            for row in self.board:
                for tile in row:
                    if tile.val == -1:
                        memoize[tile] = set()
            return memoize

        def _has_cherry(tile):
            return tile.val == 1

        def _format_solution(path):
            if self.last_tile() in path:
                cherrys_count = len(path)
                if self.last_tile().val != 1:
                    return cherrys_count - 1
                return cherrys_count
            else:
                return 0
        
        memoize_enter = _setup_memoize(defaultdict(set))
        def _solve_enter(tile: Tile) -> set([Tile]):
            if tile not in memoize_enter:
                if self.found_last(tile):
                    cherrys = _solve_exit(tile)
                    cherrys.add(tile)
                else:
                    mine_down = _solve_enter(tile.down)
                    mine_right = _solve_enter(tile.right)

                    if len(mine_down) > len(mine_right):
                        cherrys = mine_down.copy()
                    else:
                        cherrys = mine_right.copy()

                    if _has_cherry(tile):
                        cherrys.add(tile)

                memoize_enter[tile] = cherrys

            return memoize_enter[tile]                    

        memoize_exit = _setup_memoize(defaultdict(set))
        def _solve_exit(tile: Tile) -> set([Tile]):
            if tile not in memoize_exit:
                mine_up = _solve_exit(tile.up)
                mine_left = _solve_exit(tile.left)

                if len(mine_up) > len(mine_left):
                    cherrys = mine_up.copy()
                else:
                    cherrys = mine_left.copy()
                    
                if _has_cherry(tile):
                    cherrys.add(tile)
                    
                memoize_exit[tile] = cherrys
                    
            return memoize_exit[tile]

        path = _solve_enter(self.board[0][0])
        return _format_solution(path)

#-------------------------------------------------------------------------------
#   Main Driver Function for Leetcode Input
#-------------------------------------------------------------------------------
class Solution:
    def cherryPickup(self, grid: [[int]]) -> int:    
        """Main function for solving Leetcode Input

        Input:
        :mat: [[int]] -> 2D array of integers
        
        Output:
        int -> maximum number of excivated cherrys
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
        
print("\n    Unit Test")        
unittest.main()
