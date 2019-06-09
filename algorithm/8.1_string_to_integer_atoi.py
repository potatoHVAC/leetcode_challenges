#-------------------------------------------------------------------------------
#    String to Integer (atoi)
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/string-to-integer-atoi/
# Completed 6/7/19
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Extract number with regex
2. Handle no return
3. Handle too large or small
4. Return num
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

import re

def atoi(string: str) -> int:
    """Return number at start of string if exists."""
    num_str = re.match('(-|\+)?\d+', string.strip())
    if num_str is None:
        return 0

    num = int(num_str.group())
    if num < -2147483648:
        return -2147483648         
    if num > 2147483647:
        return 2147483647         
    return num

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def myAtoi(self, string: str) -> int:
        """Return number at start of string if exists.

        Input:
        :string: str -> input string
        
        Output:
        int -> output number
        """
        return atoi(string)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_42(self):
        string = "42"
        ans = 42
        self.assertEqual(Solution().myAtoi(string), ans)
    def test_42_neg(self):
        string = "-42"
        ans = -42
        self.assertEqual(Solution().myAtoi(string), ans)
    def test_42_pos(self):
        string = "+42"
        ans = 42
        self.assertEqual(Solution().myAtoi(string), ans)
    def test_space_1(self):
        string = "   1"
        ans = 1
        self.assertEqual(Solution().myAtoi(string), ans)
    def test_space_words_num(self):
        string = "a   1"
        ans = 0
        self.assertEqual(Solution().myAtoi(string), ans)
    def test_1_words(self):
        string = "1 words"
        ans = 1
        self.assertEqual(Solution().myAtoi(string), ans)
    def test_too_small(self):
        string = "-91283472332"
        ans = -2147483648
        self.assertEqual(Solution().myAtoi(string), ans)
    def test_too_large(self):
        string = "91283472332"
        ans = 2147483647
        self.assertEqual(Solution().myAtoi(string), ans)
        
unittest.main()
