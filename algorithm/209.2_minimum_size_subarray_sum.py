# Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/
# Completed 4/28/19

class Solution:
    def minSubArrayLen(self, target: int, numbers: [int]) -> int:
        if sum(numbers) < target: return 0

        left, right = 0, 0
        subarray_sum = numbers[0]
        subarray_len = len(numbers)

        while left < len(numbers):
            if subarray_sum < target:
                if right == len(numbers) - 1: return subarray_len
                right += 1
                subarray_sum += numbers[right]
            else:
                subarray_len = min(subarray_len, right - left + 1)
                subarray_sum -= numbers[left]
                left += 1

        return subarray_len
