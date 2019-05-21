# Number of Islands
# https://leetcode.com/problems/number-of-islands/
# Completed 5/21/19

#-------------------------------------------------------------------------------
#    Approach
#-------------------------------------------------------------------------------

"""
1. Create Tile, Island, and Board objects.
2. Board will have tiles for each point on the map.
3. Establish relationships between tiles by pointing [left, right, up, down]
    at their respective neighbors.
4. Populate islands on all land objects
  4.1 Scan all tiles and find any with a land indicator.
  4.2 Create Island object
  4.3 Set tile.val = Island()
  4.4 DFS style search all neighbors and replace their val with the island
       from 4.3
5. Count all unique island objects (maintain counter as they are created)
"""

#-------------------------------------------------------------------------------
#    Solution
#-------------------------------------------------------------------------------

class Tile:
    def __init__(self, val: int):
        self.val = val
        self.up = None
        self.down = None
        self.left = None
        self.right = None

class Island:
    def __init__(self):
        self.size = 0

    def add_tile(self):
        self.size += 1

class Board:
    def __init__(self, grid: [[str]]):
        """Create board and populate islands.

        Input:
        :grid: [[str]] -> 2D array of map markers
        """
        self.islands = set()
        self.map = [ row.copy() for row in grid ]
        self.draw_map().populate_relationships().expand_islands()

    def draw_map(self) -> 'self':
        """Convert marker into Tile object."""
        for row in range(0, len(self.map)):
            for col in range(0, len(self.map[0])):
                self.map[row][col] = Tile(int(self.map[row][col]))
        return self

    def populate_relationships(self) -> 'self':
        """Add neighboring tile relationships."""
        for row in range(0, len(self.map)):
            for col in range(0, len(self.map[0])):
                tile = self.map[row][col]

                if row > 0:
                    tile.up = self.map[row -1][col]
                if row < len(self.map) - 1:
                    tile.down = self.map[row + 1][col]
                if col > 0:
                    tile.left = self.map[row][col - 1]
                if col < len(self.map[0]) - 1:
                    tile.right = self.map[row][col + 1]
        return self

    def expand_islands(self) -> 'self':
        """Use DFS to populate tiles with islands."""

        def _expand_island(tile, island):
            """Spread island to neighboring tiles."""
            if tile is None:
                pass
            elif tile.val == 1:
                island.add_tile()
                tile.val = island
                _expand_island(tile.up, island)
                _expand_island(tile.down, island)
                _expand_island(tile.left, island)                
                _expand_island(tile.right, island)
                
        def _create_island(tile):
            """Create new island and spread to neighbors if 'val = 1' is found."""
            if tile.val == 1:
                island = Island()
                self.islands.add(island)
                _expand_island(tile, island)

        for row in self.map:
            for tile in row:
                _create_island(tile)
        return self

    def solve(self) -> int:
        """Return the number of islands on the map."""
        return len(self.islands)

#-------------------------------------------------------------------------------
#    Leetcode Driver
#-------------------------------------------------------------------------------

class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        return Board(grid).solve()
        
#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class testSolution(unittest.TestCase):

    def test_1(self):
        raw_map = [
            [1]
        ]
        self.assertEqual(Board(raw_map).solve(), 1)
    def test_2(self):
        raw_map = [
            [0]
        ]
        self.assertEqual(Board(raw_map).solve(), 0)
    def test_3(self):
        raw_map = [
            [1,0],
            [0,1]
        ]
        self.assertEqual(Board(raw_map).solve(), 2)
    def test_4(self):
        raw_map = [
            [1,0],
            [1,1]
        ]
        self.assertEqual(Board(raw_map).solve(), 1)        
    def test_5(self):
        raw_map = [
            [1,1],
            [1,1]
        ]
        self.assertEqual(Board(raw_map).solve(), 1)

unittest.main()
