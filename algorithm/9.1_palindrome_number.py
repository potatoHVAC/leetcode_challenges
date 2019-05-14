# Palindrome Number
# https://leetcode.com/problems/palindrome-number/
# Completed 5/9/19

"""Approach
1. Convert integer into string.
2. Check if that string is equal to its self in reverse.
"""

class Solution:
    def isPalindrome(self, input_int: int) -> bool:
        """Check if the input integer is a palindrome

        Input:
        :input_int: int -- integer to check
        
        Output:
        True -- if :input_int: is a palindrome
        """
        return str(input_int) == self.reverse_str(str(input_int))

    def reverse_str(self, string: str) -> str:
        """Return the input string in reverse order"""
        return "".join([ char for char in string ][::-1])

#-------------------------------------------------------------------------------

import unittest

class TestIsPalindrome(unittest.TestCase):

    def test_1(self):
        self.assertTrue(Solution().isPalindrome(4))
    def test_121(self):
        self.assertTrue(Solution().isPalindrome(121))
    def test_11(self):
        self.assertTrue(Solution().isPalindrome(11))
    def test_12(self):
        self.assertFalse(Solution().isPalindrome(12))
    def test_1221(self):
        self.assertTrue(Solution().isPalindrome(1221))        
    def test_negative(self):
        self.assertFalse(Solution().isPalindrome(-5))    

if __name__ == '__main__':
    unittest.main()
