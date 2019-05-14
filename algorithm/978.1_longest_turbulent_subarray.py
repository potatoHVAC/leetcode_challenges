# Longest Turbulent Subarray
# https://leetcode.com/problems/longest-turbulent-subarray/
# Completed 5/9/19

"""Approach
1. Create a compare function that does <=>.
2. Itterate through the input list.
  2.1 Check the direction of sigh change with compare.
  2.2 If sign change is different than previous, increase length counter.
    2.2.1 update max found with length counter if counter is larger.
  2.3 if sign change is same or numbers are equal, reset length counter.
3. Return max length
"""

def compare(num1: int, num2: int) -> int:
    """Compare two numbers and return their relative direction.

    Input:
    :num1: int
    :num2: int

    Output:
    1  -- if :num1: < :num2:
    -1 -- if :num1: > :num2:
    0  -- if :num1: == :num2: 
    """
    if num1 < num2: return 1
    elif num1 > num2: return -1
    else: return 0

class Solution:
    def maxTurbulenceSize(self, series: [int]) -> int:
        """Return the max lenght of a terbulent subseries.

        Input:
        :series: [int] -- list of integers

        Output:
        int -- length of the longest subseries of the input series
        """
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
