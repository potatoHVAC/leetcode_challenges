# Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/
# Almost completed 4/27/19
# Fails with large inputs due to recursive depth size

class Solution:
    def minSubArrayLen(self, target: int, numbers: [int]) -> int:
        if sum(numbers) < target: return 0
    
        def _min_sub_array_len(target, numbers, min_len = len(numbers), left: int = 0, right: int = 0) -> int:
            # Find min sub array lenght recursively with left and right pointers.
            if right > len(numbers): return min_len
            
            if sum(numbers[left:right]) < target:
                return _min_sub_array_len(target, numbers, min_len, left, right + 1)
            else:
                new_min_len = min([min_len, right - left])
                return _min_sub_array_len(target, numbers, new_min_len, left + 1, right)

        return _min_sub_array_len(target, numbers)
