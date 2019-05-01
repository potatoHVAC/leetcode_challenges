# Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/
# Completed 4/28/19

class Solution:
    def intersection(self, nums1: [int], nums2: [int]) -> [int]:
        nums1_dict = self.count_elements_in(nums1)
        return self.compare_array_to_dict(nums2, nums1_dict)
        
    def count_elements_in(self, array: [int]) -> dict:
        '''
        Create dictionary from array elements
          key:   integer
          value: count of key in array        
        '''
        numbers = {}
        for num in array:
            if num in numbers: numbers[num] += 1
            else: numbers[num] = 0

        return numbers

    def compare_array_to_dict(self, array: [int], dictionary: dict) -> [int]:
        intersect = set()
        for num in array:
            if num in dictionary: intersect.add(num)
        return list(intersect)
