# Sqrt(x)
# https://leetcode.com/problems/sqrtx/
# Almost complete 4/20/19
# This is a brute force method and will time out for large inputs.

"""Approach
1. multiply the input by 100
2. Itterate i up from 1
  2.1 find the first number that square is larger than input**100
  2.2 return (i-1)//10
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        """Return the integer square root of x

        Input:
        :x: int -- number to find the square root 

        Output:
        int -- integer value of the square root rounded down
        """
        if x == 0: return 0
        hundred_x = x * 100
        for i in range(1, hundred_x):
            if i ** 2 > hundred_x:
                return (i - 1) // 10
