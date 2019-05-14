# Heaters
# https://leetcode.com/problems/heaters/
# Completed 4/25/19

class Neighborhood:
    def __init__(self, houses: [int], heaters: [int]):
        self.houses = houses
        self.heaters = heaters
        self.heater_radius = 0

    def get_required_range(self, house_pointer: int, heater_pointer: int) -> int:
        """Return distance between house and heater."""
        return abs(self.houses[house_pointer] - self.heaters[heater_pointer])
        
    def more_heaters_exist(self, heater_pointer: int) -> bool:
        """Return True if more heaters exist"""
        return heater_pointer < len(self.heaters) - 1

    def update_heater_radius(self, house_pointer: int, heater_pointer: int):
        """Update the minimum required distance given the input house and heater"""
        if self.more_heaters_exist(heater_pointer):
            required_range = min(
                self.get_required_range(house_pointer, heater_pointer),
                self.get_required_range(house_pointer, heater_pointer + 1)
            )
        else:
            required_range = self.get_required_range(house_pointer, heater_pointer)

        self.heater_radius = max(self.heater_radius, required_range)

    def find_heater_radius(self, house_pointer: int = 0, heater_pointer: int = 0) -> int:
        """Find the minimum required heater radius using recursion"""
        if house_pointer == len(self.houses):
            return self.heater_radius

        # Advance heater pointer if more heaters exist and the house is to the right of the heaters.
        if self.more_heaters_exist(heater_pointer)\
        and self.houses[house_pointer] > self.heaters[heater_pointer + 1]:
            return self.find_heater_radius(house_pointer, heater_pointer + 1)

        # Evaluate current house then advance the house pointer.
        else:
            self.update_heater_radius(house_pointer, heater_pointer)
            return self.find_heater_radius(house_pointer + 1, heater_pointer)
        
class Solution:
    def findRadius(self, houses: [int], heaters: [int]) -> int:
        """Return the minimum required radius to cover all houses with heaters.

        Input:
        :houses:  [int] -- list of integers representing house locations
        :heaters: [int] -- list of integers representing heater locations

        Output:
        int -- value of the minimum required heater radius to cover all houses
        """
        houses.sort()
        heaters.sort()
        return Neighborhood(houses, heaters).find_heater_radius()
    
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_findRadius_1to1_small_heater(self):
        self.assertEqual(Solution().findRadius([1], [1]), 0)
    def test_findRadius_2to2_small_heater(self):
        self.assertEqual(Solution().findRadius([1, 5], [1, 5]), 0)
    def test_findRadius_1to1_large_heater(self):
        self.assertEqual(Solution().findRadius([1], [50]), 49)
    def test_findRadius_2to2_large_heater(self):
        self.assertEqual(Solution().findRadius([1, 100], [50, 51]), 49)
    def test_findRadius_heaters_outside_houses(self):
        self.assertEqual(Solution().findRadius([2, 3], [1, 4]), 1)
    def test_findRadius_heaters_before_houses(self):
        self.assertEqual(Solution().findRadius([3, 4], [1]), 3)
    def test_findRadius_example_1(self):
        self.assertEqual(Solution().findRadius([1, 2, 3], [2]), 1)
    def test_findRadius_example_2(self):
        self.assertEqual(Solution().findRadius([1, 2, 3, 4], [1, 4]), 1)

unittest.main()
