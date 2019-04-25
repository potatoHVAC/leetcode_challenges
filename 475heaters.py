# Heaters
# https://leetcode.com/problems/heaters/
# Completed 4/25/19

class Neighborhood:
    def __init__(self, houses, heaters):
        self.houses = houses
        self.heaters = heaters
        self.heater_radius = 0

    def get_required_range(self, house_i, heater_i):
        '''
        input:  house_i  -> int -- house index
                heater_i -> int -- heater index
        output: int             -- distance from heater to house
        '''
        return abs(self.houses[house_i] - self.heaters[heater_i])
        
    def more_heaters_exist(self, heater_i):
        '''
        input:  int  -- heater index
        output: bool -- False if index points to last heater
        '''
        return heater_i < len(self.heaters) - 1

    def update_heater_radius(self, house_i, heater_i):
        '''
        input:  house_i  -> int -- house index
                heater_i -> int -- heater index

        Updates the minimum required distance for full heater coverage.
        '''
        if self.more_heaters_exist(heater_i):
            required_range = min(
                self.get_required_range(house_i, heater_i),
                self.get_required_range(house_i, heater_i + 1)
            )
        else:
            required_range = self.get_required_range(house_i, heater_i)

        self.heater_radius = max(self.heater_radius, required_range)

    def find_heater_radius(self, house_i = 0, heater_i = 0):
        '''
        input:  house_i  -> int -- house index
                heater_i -> int -- heater index
        output: int             -- minimum required range for heaters to cover all houses
        '''
        if house_i == len(self.houses):
            return self.heater_radius

        # Advance heater pointer if more heaters exist and the house is to the right of the heaters.
        if self.more_heaters_exist(heater_i) and self.houses[house_i] > self.heaters[heater_i + 1]:
            return self.find_heater_radius(house_i, heater_i + 1)

        # Evaluate current house then advance the house pointer.
        else:
            self.update_heater_radius(house_i, heater_i)
            return self.find_heater_radius(house_i + 1, heater_i)
        
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        neighborhood = Neighborhood(houses, heaters)
        return neighborhood.find_heater_radius()
    
