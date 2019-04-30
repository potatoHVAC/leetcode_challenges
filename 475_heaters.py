# Heaters
# https://leetcode.com/problems/heaters/
# Completed 4/25/19

class Neighborhood:
    def __init__(self, houses: [int], heaters: [int]):
        self.houses = houses
        self.heaters = heaters
        self.heater_radius = 0

    def get_required_range(self, house_pointer: int, heater_pointer: int) -> int:
        # Return distance from house to heater given their pointers
        return abs(self.houses[house_pointer] - self.heaters[heater_pointer])
        
    def more_heaters_exist(self, heater_pointer: int) -> bool:
        # Return True if heater pointer does not point at last heater
        return heater_pointer < len(self.heaters) - 1

    def update_heater_radius(self, house_pointer: int, heater_pointer: int):
        # Updates the minimum required distance for full heater coverage.
        if self.more_heaters_exist(heater_pointer):
            required_range = min(
                self.get_required_range(house_pointer, heater_pointer),
                self.get_required_range(house_pointer, heater_pointer + 1)
            )
        else:
            required_range = self.get_required_range(house_pointer, heater_pointer)

        self.heater_radius = max(self.heater_radius, required_range)

    def find_heater_radius(self, house_pointer: int = 0, heater_pointer: int = 0) -> int:
        # Return minimum heater radius
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
        houses.sort()
        heaters.sort()
        return Neighborhood(houses, heaters).find_heater_radius()
    
