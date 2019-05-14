# Sort an Array
# https://leetcode.com/problems/sort-an-array/
# Completed 4/30/19
# Quick Sort

"""Approach
1. Impliment 'bad' quick sort recursively.
2. select a random pivot.
3. Collect all numbers below pivot value
4. collect all number == pivot value
5. Collect all numbers above pivot value
6. Repeate steps 3 through 5 on the output from step 3 and the output from step 5
7. repeat(step 3) + step 4 + repeat(step 5) 
8. return array

This is 'bad' because it keeps creating new arrays for each iteration of the sort
negating the space and time saving advantages of quick sort when using pointers.
"""

class Solution:
    def sortArray(self, numbers: [int]) -> [int]:
        return self.quick_sort(numbers)

    def quick_sort(self, numbers: [int]) -> [int]:
        """Return sorted array.

        Input:
        :numbers: [int] -- list of unsorted integers

        Output:
        [int] -- list of sorted integers
        """
        if not numbers: return numbers
        pivot = len(numbers) // 2
        
        return (
            self.quick_sort([ num for num in numbers if num < numbers[pivot] ]) +\
            [ num for num in numbers if num == numbers[pivot] ] +\
            self.quick_sort([ num for num in numbers if num > numbers[pivot] ])
        )

