# Sort an Array
# https://leetcode.com/problems/sort-an-array/
# Completed 4/25/19 With time out on large input test case
# Bubble Sort 

"""Approach
1. Implement bubble sort
2. Itterate through array
  2.1 if adjacent numbers are out of order, flip those numbers
3. If setp 2 is complete and a flip occured, repeat step 2
4. return array
"""

class Solution:
    def sortArray(self, numbers: [int]) -> [int]:
        return self.bubble_sort(numbers)

    def bubble_sort(self, numbers: [int]) -> [int]:
        """Return sorted array.

        Input:
        :numbers: [int] -- list of unsorted integers

        Output:
        [int] -- list of sorted integers
        """
        unsorted = True
        while unsorted:
            unsorted = False
            for i in range(1, len(numbers)):
                if numbers[i] < numbers[i - 1]:
                    unsorted = True
                    numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]

        return numbers
