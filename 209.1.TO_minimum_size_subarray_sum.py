# Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/
# Almost completed 4/27/19
# Fails with large inputs due to recursive depth size

def min_subarray(arr, target):
    if sum(arr) < target: return 0
    
    def _min_subarray(arr, target, min_found = len(arr), left = 0, right = 0):
        if right > len(arr):
            return min_found
        
        if sum(arr[left:right]) < target:
            return _min_subarray(arr, target, min_found, left, right + 1)
        else:
            return _min_subarray(arr, target, min([min_found, right - left]), left + 1, right)

    return _min_subarray(arr, target)


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        return min_subarray(nums, s)
