# Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/
# Completed 5/9/19

"""Approach: 
1. Split array on 0.
2. Reverse positive array.
3. Square both arrays.
4. Iterate over arrays adding the next lowest element to output array.
"""

def find_zero(arr: list) -> int:
    """Find the index of the first positive number in input list. Return the length of 
    the list if all elements are negative
    """
    for i, ele in enumerate(arr):
        if ele >= 0: return i
    return len(arr)

def combine(arrays: [list, list]) -> list:
    """Combine two lists into one sorted list. Input lists must be sorted in decending 
    order. Only the first two lists in :arrays: will be comibined, additional lists will 
    be ignored.

    Input:
    :arrays: [list, list] -- list of integer lists
    
    Output:
    list -- sorted list
    """
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
    """Split a sorted array on the first zero and return the seperate arrays. Reverse the
    negative array before returning. Input array must be in sorted order.
    """
    pivot = find_zero(arr)
    lower = arr[:pivot]
    upper = arr[pivot:]
    upper.reverse()
    return [lower, upper]

def square_arrays(arrays: [list]) -> [list]:
    """Return list of lists where each element is squared"""
    output = []
    for array in arrays:
        output.append(list(map(lambda num: num**2, array)))
    return output

class Solution:
    def sortedSquares(self, array: [int]) -> [int]:
        return combine(square_arrays(split_array_on_sign(array)))
        
