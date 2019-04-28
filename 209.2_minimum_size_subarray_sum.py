# Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/
# Completed 4/28/19

def min_subarray(arr, target):
    '''
    input:  arr    -> list[int] 
            target -> int       -- maximum sum
    output: int                 -- length of minimum subarray

    Returns the length of the minumum subarray with its sum >= target
    '''
    if sum(arr) < target: return 0

    left, right = 0, 0
    subarray_sum = arr[0]
    subarray_len = len(arr)

    while left < len(arr):
        if subarray_sum < target:
            if right == len(arr) - 1: return subarray_len
            right += 1
            subarray_sum += arr[right]
        else:
            subarray_len = min(subarray_len, right - left + 1)
            subarray_sum -= arr[left]
            left += 1

    return subarray_len

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        return min_subarray(nums, s)
