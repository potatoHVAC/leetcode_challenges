#-------------------------------------------------------------------------------
#    Reverse Integer
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/reverse-integer/
# Completed 6/7/19
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Turn the input postitive.
2. Pop off last integer from target.
3. Add that to 10 times the answer.
4. Repeat until target is empty.
5. Turn answer negative if needed.
6. Return answer if in range.
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def my_reverse(num: int) -> int:
    """Return integer with reversed numbers"""
    target_num = abs(num)

    ans = 0
    while target_num != 0:
        pop_int = target_num % 10
        target_num = target_num // 10
        ans = 10 * ans + pop_int

    ans *= num // abs(num)
        
    if ans not in range(-2147483648, 2147483648):
        return 0        
    return ans

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def reverse(self, x: int) -> int:
        """Return integer with reversed numbers
        
        Input:
        :x: int -> input number

        Output:
        int -> reversed input number
        """
        return my_reverse(x)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_1(self):
        num = 1
        ans = 1
        self.assertEqual(Solution().reverse(num), ans)
    def test_123(self):
        num = 123
        ans = 321
        self.assertEqual(Solution().reverse(num), ans)
    def test_1_neg(self):
        num = -1
        ans = -1
        self.assertEqual(Solution().reverse(num), ans)
    def test_123_neg(self):
        num = -123
        ans = -321
        self.assertEqual(Solution().reverse(num), ans)
    def test_ob(self):
        num = 1123456789
        ans = 0
        self.assertEqual(Solution().reverse(num), ans)
        
unittest.main()
