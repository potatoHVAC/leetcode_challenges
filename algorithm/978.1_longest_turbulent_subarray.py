# Longest Turbulent Subarray
# https://leetcode.com/problems/longest-turbulent-subarray/
# Completed 5/9/19

def compare(num1: int, num2: int) -> int:
    if num1 < num2: return 1
    elif num1 > num2: return -1
    else: return 0

class Solution:
    def maxTurbulenceSize(self, series: [int]) -> int:
        # Return the length of the longest turbulent sub array.
        max_length = overall_max = 1
        previous_sign_change = None
        
        for i, num in enumerate(series[1:]):
            sign_change = compare(series[i], num)
            
            if previous_sign_change != sign_change and 0 not in [previous_sign_change, sign_change]:
                max_length += 1
                overall_max = max(overall_max, max_length)
            else:
                max_length = 2
            previous_sign_change = sign_change
            
        return overall_max
