#-------------------------------------------------------------------------------
#   Cherry Picking
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://github.com/potatoHVAC/leetcode_challenges/tree/master/algorithm
# Completed 6/9/19
#-------------------------------------------------------------------------------
#   Solution
#-------------------------------------------------------------------------------

from collections import defaultdict

class Tile:
    def __init__(self, val, row, col):
        self.val = val
        self.id = (row, col)
        self.right = None
        self.down = None

class Bushel:

    def __init__(self, cherries: int):
        self.cherries = cherries

class Orchard:
    def __init__(self, mat):
        self.orchard = [ row.copy() for row in mat ]
        self.memoize = {'dead_end': Bushel(None)}        
        self._build_orchard(mat)._set_relationships()._set_last()._solve()

    def _set_last(self) -> 'self':
        """Set memoize for final tile"""
        if self.last_tile().val != -1:
            key = str(self.last_tile().id) * 2
            self.memoize[key] = Bushel(self.last_tile().val)
        return self

    def _build_orchard(self, mat) -> 'self':
        """Populate orchard tiles with values."""
        for row in range(0, len(mat)):
            for col in range(0, len(mat[0])):
                self.orchard[row][col] = Tile(mat[row][col], row, col)
        return self

    def _set_relationships(self) -> 'self':
        """Populate tile relationships"""
        for row in range(0, len(self.orchard)):
            for col in range(0, len(self.orchard[0])):
                tile = self.orchard[row][col]

                if row < len(self.orchard) - 1:
                    tile.down = self.orchard[row + 1][col]
                if col < len(self.orchard[0]) - 1:
                    tile.right = self.orchard[row][col + 1]
        return self

    def last_tile(self) -> Tile:
        """Return last tile object"""
        row = len(self.orchard) - 1
        col = len(self.orchard[0]) - 1
        return self.orchard[row][col]
    
    def found_last(self, tile: Tile) -> bool:
        """Return True if tile is the end of the mine"""
        return tile == self.last_tile()

    def _memoize_key_gen(self, tile1: Tile, tile2: Tile) -> str:
        """Return a unique key for memoization."""
        if tile1 is None or tile2 is None or tile1.val == -1 or tile2.val == -1:
            return 'dead_end'
        elif tile1.id[0] < tile2.id[0]:
            return ''.join([str(tile1.id), str(tile2.id)])
        return ''.join([str(tile2.id), str(tile1.id)])

    def _max_bushel(self, bushels: [Bushel]) -> Bushel:
        """Return the bushel with the most cherries."""
        valid_bushels = [ bushel for bushel in bushels if bushel.cherries is not None ]
        if valid_bushels:
            return Bushel(max([ bushel.cherries for bushel in valid_bushels ]))
        return Bushel(None)

    def _add_cherries(self, tile1: Tile, tile2: Tile, bushel: Bushel) -> Bushel:
        """Insert cherries into bushel."""
        if bushel.cherries is not None:
            bushel.cherries += tile1.val
            if tile1 != tile2:
                bushel.cherries += tile2.val
        return bushel

    def _solve(self) -> Bushel:
        """DFS solve with two paths."""

        def __solve(tile1: Tile, tile2: Tile) -> Bushel:
            key = self._memoize_key_gen(tile1, tile2)
            if key not in self.memoize:
                bushels = []
                bushels.append(__solve(tile1.right, tile2.right))
                bushels.append(__solve(tile1.down, tile2.down))
                bushels.append(__solve(tile1.right, tile2.down))
                if tile1 != tile2:
                    bushels.append(__solve(tile1.down, tile2.right))

                self.memoize[key] = self._add_cherries(
                    tile1,
                    tile2,
                    self._max_bushel(bushels)
                )
                
            return self.memoize[key]

        return __solve(self.orchard[0][0], self.orchard[0][0])

    def ans(self) -> int:
        """Return number of cherries picked."""
        bushel = self._solve()
        if bushel.cherries:
            return bushel.cherries
        return 0

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
        return Orchard(grid).ans()

#-------------------------------------------------------------------------------
#   Test
#-------------------------------------------------------------------------------

import unittest

class TestOrchard(unittest.TestCase):

    def test_simple(self):
        mat = [
            [ 0, 1],
            [-1, 0]
        ]
        self.assertEqual(Orchard(mat).ans(), 1)
    def test_dont_double_count_path(self):
        mat = [
            [ 1, 1],
            [-1, 1]
        ]
        self.assertEqual(Orchard(mat).ans(), 3)
    def test_all_1(self):
        mat = [
            [ 1, 1],
            [ 1, 1]
        ]
        self.assertEqual(Orchard(mat).ans(), 4)
    def test_all_walls_except_start(self):
        mat = [
            [ 1,-1],
            [-1,-1]
        ]
        self.assertEqual(Orchard(mat).ans(), 0)
    def test_single_1(self):
        mat = [[1]]
        self.assertEqual(Orchard(mat).ans(), 1)
    def test_single_wall(self):
        mat = [[-1]]
        self.assertEqual(Orchard(mat).ans(), 0)
    def test_single_0(self):
        mat = [[0]]
        self.assertEqual(Orchard(mat).ans(), 0)           
    def test_start_is_wall(self):
        mat = [
            [-1, 1],
            [ 1, 1]
        ]
        self.assertEqual(Orchard(mat).ans(), 0)
    def test_end_is_wall(self):
        mat = [
            [ 1, 0],
            [ 0,-1]
        ]
        self.assertEqual(Orchard(mat).ans(), 0)
    def test_empty_rectangle(self):
        mat = [
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(Orchard(mat).ans(), 0)
    def test_multiple_paths(self):
        mat = [
            [ 0, 0, 0, 0, 0],
            [ 1,-1, 1,-1, 1],
            [ 0, 0, 0, 0, 0]
        ]
        self.assertEqual(Orchard(mat).ans(), 2)
    def test_sparse(self):
        mat = [
            [ 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0],            
            [ 0, 0, 1, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0],
            [ 1, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(Orchard(mat).ans(), 2)
    def test_barrior(self):
        mat = [
            [ 1, 1, 1, 1,-1, 1],
            [ 1, 1, 1,-1, 1, 1],            
            [ 1, 1,-1, 1, 1, 1],
            [ 1,-1, 1, 1, 1, 1],
            [-1, 1, 1, 1, 1, 1]
        ]
        self.assertEqual(Orchard(mat).ans(), 0)
    def test_find_max_path1(self):
        mat = [
            [ 0, 0, 0, 1, 1, 1],
            [ 1,-1, 1, 0, 0, 0],
            [ 1,-1,-1,-1,-1, 0],
            [ 1, 1, 1, 1, 1, 0]
        ]
             
        self.assertEqual(Orchard(mat).ans(), 10)
    def test_find_max_path_2(self):
        mat = [
            [ 0, 0, 0, 0, 0, 1],
            [ 0,-1, 1, 0, 0, 0],            
            [ 1,-1, 1, 0, 0, 0],
            [ 1,-1,-1,-1,-1, 0],
            [ 1, 1, 1, 1, 1, 0]
        ]
        self.assertEqual(Orchard(mat).ans(), 9)            
    def test_find_max_path3(self):
        mat = [
            [ 0, 1, 0, 1, 1, 1],
            [ 0,-1, 0, 0, 0, 0],            
            [ 0,-1, 1, 1, 1, 0],
            [ 0,-1,-1,-1,-1, 1],
            [ 1, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(Orchard(mat).ans(), 8)
    def test_find_max_path4(self):
        mat = [
            [ 0, 1, 0, 1, 1, 1],
            [ 0,-1, 0, 0, 0, 0],            
            [ 0,-1, 1, 1, 1, 0],
            [ 0,-1,-1,-1,-1, 1],
            [ 1, 1, 0, 0, 0, 0]
        ]
        self.assertEqual(Orchard(mat).ans(), 8)
    def test_find_max_path5(self):
        mat = [
            [ 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 1, 1],            
            [ 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 1, 1]
        ]
        self.assertEqual(Orchard(mat).ans(), 18)
    def test_find_max_path6(self):
        mat = [
            [ 1, 1, 1, 1,-1, 1],
            [ 1, 1, 1,-1, 1, 1],            
            [ 1, 1, 1, 1, 1, 1],
            [ 1,-1, 1, 1, 1, 1],
            [-1, 1, 1, 1, 1, 1]
        ]
        self.assertEqual(Orchard(mat).ans(), 17)
    def test_find_max_path7(self):
        mat = [
            [ 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1,-1, 1, 1],            
            [ 1, 1, 1, 1, 1, 1],
            [ 1,-1, 1, 1, 1, 1],
            [-1, 1, 1, 1, 1, 1]
        ]
        self.assertEqual(Orchard(mat).ans(), 18)
    def test_find_max_path8(self):
        mat = [
            [ 1, 1, 0, 1],
            [ 1,-1, 1, 0],            
            [ 0,-1,-1, 0],
            [ 0, 1,-1, 1],
            [ 1, 0, 1, 1]
        ]
        self.assertEqual(Orchard(mat).ans(),  8)
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
        self.assertEqual(Orchard(mat).ans(), 15)
    def test_large(self):
        mat = [
            [ 1, 1, 1, 1,-1, 1,-1,-1,-1, 0],
            [ 1, 1, 1, 0, 1, 0, 0, 1, 1,-1],
            [-1,-1,-1, 1, 1, 1,-1, 1, 1, 1],
            [-1, 1, 1, 1, 1, 1, 1,-1, 1, 1],
            [ 0, 0, 1, 0, 1,-1, 1, 0, 1, 1],
            [ 1, 0, 1, 1,-1, 0, 0, 1, 1, 0],
            [ 1, 1, 0, 1, 0, 0, 1, 1, 1,-1],
            [ 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [ 1, 0, 1, 0,-1, 1, 1, 1, 1, 0],
            [ 1, 0,-1, 0, 1, 0, 1,-1, 0, 1]
        ]
        self.assertEqual(Orchard(mat).ans(), 30)
    def test_find_max_path10(self):
        mat = [
            [ 1, 1, 1, 1,-1,-1,-1, 1, 0, 0],
            [ 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [ 0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
            [ 1, 1, 0, 1, 1, 1, 0,-1, 1, 1],
            [ 0, 0, 0, 0, 1,-1, 0, 0, 1,-1],
            [ 1, 0, 1, 1, 1, 0, 0,-1, 1, 0],
            [ 1, 1, 0, 1, 0, 0, 1, 0, 1,-1],
            [ 1,-1, 0, 1, 0, 0, 0, 1,-1, 1],
            [ 1, 0,-1, 0,-1, 0, 0, 1, 0, 0],
            [ 0, 0,-1, 0, 1, 0, 1, 0, 0, 1]
        ]
        self.assertEqual(Orchard(mat).ans(), 22)      
        
unittest.main()
