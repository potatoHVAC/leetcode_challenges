# Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/
# Completed 5/9/19

##### Approach: 
# split array on 0
# reverse positive array
# square both arrays
# iterate over arrays adding the next lowest element to output array

def find_zero(arr: list) -> int:
    # Return index of the first number where 'number >= 0'.
    # If all numbers are negative, return length of list.
    for i, ele in enumerate(arr):
        if ele >= 0: return i
    return len(arr)

def combine(arrays: [list, list]) -> list:
    # Return sorted list that is the combination of 2 input lists.
    # Input lists must be sorted and in decending order.
    def _combine(arr1: list, arr2: list, output: list) -> list:
        if len(arr1) == 0 or len(arr2) == 0:
            # Exit recursion if either list is empty.
            arr1.reverse()
            arr2.reverse()
            return output + arr1 + arr2
    
        if arr1[-1] < arr2[-1]: 
            output.append(arr1.pop())
        else:
            output.append(arr2.pop())

        return _combine(arr1, arr2, output)
    return _combine(arrays[0], arrays[1], [])

def split_array_on_sign(arr: list) -> [list]:
    # Return two arrays sorted in decending order that are split on the number where 'number >= 0'.
    # Input array must be sorted in ascending order.
    pivot = find_zero(arr)
    lower = arr[:pivot]
    upper = arr[pivot:]
    upper.reverse()
    return [lower, upper]

def square_arrays(arrays: [list]) -> [list]:
    # Return list of lists where each list element is squared.
    output = []
    for array in arrays:
        output.append(list(map(lambda num: num**2, array)))
    return output

class Solution:
    def sortedSquares(self, array: List[int]) -> List[int]:
        return combine(square_arrays(split_array_on_sign(array)))
        
