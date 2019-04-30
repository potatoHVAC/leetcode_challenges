# Sort an Array
# https://leetcode.com/problems/sort-an-array/
# Completed 4/30/19
# Quick Sort
    
class Solution:
    def sortArray(self, numbers: [int]) -> [int]:
        return self.quick_sort(numbers)

    def quick_sort(self, numbers: [int]) -> [int]:
        # Return sorted array of numbers
        if not numbers: return numbers
        pivot = len(numbers) // 2
        
        return (
            self.quick_sort([ num for num in numbers if num < numbers[pivot] ]) +\
            [ num for num in numbers if num == numbers[pivot] ] +\
            self.quick_sort([ num for num in numbers if num > numbers[pivot] ])
        )

