# Sort an Array
# https://leetcode.com/problems/sort-an-array/
# Completed 4/25/19 With time out on large input test case
# Bubble Sort 

class Solution:
    def sortArray(self, numbers: [int]) -> [int]:
        return self.bubble_sort(numbers)

    def bubble_sort(self, numbers: [int]) -> [int]:
        # Return sorted array of numbers
        unsorted = True
        while unsorted:
            unsorted = False
            for i in range(1, len(numbers)):
                if numbers[i] < numbers[i - 1]:
                    unsorted = True
                    numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]

        return numbers
