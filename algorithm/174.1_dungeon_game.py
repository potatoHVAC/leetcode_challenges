#-------------------------------------------------------------------------------
#    Dungon Game
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/dungeon-game/
# Completed 6/19/19
#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

class Dungeon:

    def __init__(self, dungeon: [[int]]):
        self.dungeon = dungeon

    def update(self, row, col, health):
        """Update position with minimum required health"""
        new_health = health - self.dungeon[row][col]
        if new_health < 1:
            self.dungeon[row][col] = 1
        else:
            self.dungeon[row][col] = new_health

    def set_last(self):
        """Update health for the princes position."""
        self.update(len(self.dungeon) - 1, len(self.dungeon[0]) - 1, 1)

    def set_col(self):
        """Update all columns in the bottom row."""
        row = len(self.dungeon) - 1
        col = len(self.dungeon[0]) - 2
        while col >= 0:
            self.update(row, col, self.dungeon[row][col + 1])
            col -= 1

    def set_row(self):
        """Update all rows in the last column."""
        row = len(self.dungeon) - 2
        col = len(self.dungeon[0]) - 1
        while row >= 0:
            self.update(row, col, self.dungeon[row + 1][col])
            row -= 1

    def set_all(self):
        """Update all positions not in the last or or last column."""
        row = len(self.dungeon) - 2
        while row >= 0:
            col = len(self.dungeon[0]) - 2
            while col >= 0:
                min_health = min(self.dungeon[row+1][col], self.dungeon[row][col+1])
                self.update(row, col, min_health)
                col -= 1
            row -= 1
        
    def solve(self) -> int:
        """Update all positions and return the minimum health for the knight."""
        self.set_last()
        self.set_col()
        self.set_row()
        self.set_all()
        return self.dungeon[0][0]

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def calculateMinimumHP(self, dungeon: [[int]]) -> int:
        return Dungeon(dungeon).solve()

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_1(self):
        dungeon = [[-5]]
        ans = 6
        self.assertEqual(Solution().calculateMinimumHP(dungeon), ans)
    def test_2(self):
        dungeon = [[5]]
        ans = 1
        self.assertEqual(Solution().calculateMinimumHP(dungeon), ans)
    def test_3(self):
        dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
        ans = 7
        self.assertEqual(Solution().calculateMinimumHP(dungeon), ans)

unittest.main()
