# Sqrt(x)
# https://leetcode.com/problems/sqrtx/
# Almost complete 4/20/19
# This is a brute force method and will time out for large inputs.

class Solution:
    def mySqrt(self, x: int) -> int:
        # Return the integer squareroot of 'x'
        if x == 0: return 0
        hundred_x = x * 100
        for i in range(1, hundred_x):
            if i ** 2 > hundred_x:
                return (i - 1) // 10
