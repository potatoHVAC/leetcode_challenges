#-------------------------------------------------------------------------------
#    Making A Large Island
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/making-a-large-island/
# Completed 6/18/19
#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

class Island:

    def __init__(self):
        self.size = 0

    def increase_size(self):
        self.size += 1

class Map:

    def __init__(self, grid: [[int]]):
        self.grid = grid
        self.populate_islands()

    def out_of_bounds(self, row: int, col: int) -> bool:
        """Return True if :row: or :col: are out of bounds."""
        return row not in range(0,len(self.grid)) \
            or col not in range(0,len(self.grid[0]))

    def skip(self, row: int, col: int) -> bool:
        """Return True if water position has water or already has Island 
        object.
        """
        return self.grid[row][col] != 1

    def populate_islands(self) -> 'self':
        """Create Island objects and spread them throughout the grid."""

        def _populate_islands(row: int, col: int, island: Island):
            if self.out_of_bounds(row, col) or self.skip(row, col):
                return

            self.grid[row][col] = island
            island.increase_size()

            _populate_islands(row + 1, col, island)
            _populate_islands(row - 1, col, island)
            _populate_islands(row, col + 1, island)
            _populate_islands(row, col - 1, island)

        for row in range(0, len(self.grid)):
            for col in range(0, len(self.grid[0])):
                _populate_islands(row, col, Island())

        return self

    def is_land(self, row: int, col: int) -> bool:
        """Return True if position contains land."""
        return self.grid[row][col] != 0

    def get_neighbors(self, row: int, col: int) -> set([Island]):
        """Return a set of all neighboring islands."""
        neighbors = set()
        if not self.out_of_bounds(row + 1, col) and self.is_land(row + 1, col):
            neighbors.add(self.grid[row + 1][col])
        if not self.out_of_bounds(row - 1, col) and self.is_land(row - 1, col):
            neighbors.add(self.grid[row - 1][col])
        if not self.out_of_bounds(row, col + 1) and self.is_land(row, col + 1):
            neighbors.add(self.grid[row][col + 1])
        if not self.out_of_bounds(row, col - 1) and self.is_land(row, col - 1):
            neighbors.add(self.grid[row][col - 1])
            
        return neighbors

    def sum_neighbors(self, neighbor_set: set([Island])) -> int:
        """Return the sum of a list of Island objects."""
        return sum([ island.size for island in neighbor_set ])

    def flip_water(self, row: int, col: int) -> int:
        """Return the resulting sum from flipping this tile if it is water."""
        if self.is_land(row, col):
            return self.grid[row][col].size
        
        neighbor_set = self.get_neighbors(row, col)
        return self.sum_neighbors(neighbor_set) + 1
        
    def largest_merger(self) -> int:
        """Return the size of the largest possible island from flipping one 
        water tile.
        """
        largest_island = 0
        for row in range(0, len(self.grid)):
            for col in range(0, len(self.grid[0])):
                largest_island = max(
                    largest_island,
                    self.flip_water(row, col)
                )

        return largest_island

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def largestIsland(self, grid: [[int]]) -> int:
        return Map(grid).largest_merger()

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_1(self):
        island = [[1]]
        ans = 1
        self.assertEqual(Solution().largestIsland(island), ans)
    def test_0(self):
        island = [[0]]
        ans = 1
        self.assertEqual(Solution().largestIsland(island), ans)
    def test_e1(self):
        island = [[1, 0], [0, 1]]
        ans = 3
        self.assertEqual(Solution().largestIsland(island), ans)
    def test_e2(self):
        island = [[1, 1], [1, 0]]
        ans = 4
        self.assertEqual(Solution().largestIsland(island), ans)
    def test_e3(self):
        island = [[1, 1], [1, 1]]
        ans = 4
        self.assertEqual(Solution().largestIsland(island), ans)
    def test_lare1(self):
        island = [
            [1, 0, 0],
            [0, 0, 0],
            [1, 0, 0]            
        ]
        ans = 3
        self.assertEqual(Solution().largestIsland(island), ans)
    def test_catch_larger_island(self):
        island = [
            [1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],            
            [0, 1, 1, 0, 1]            
        ]
        ans = 4
        self.assertEqual(Solution().largestIsland(island), ans)
        
unittest.main()
