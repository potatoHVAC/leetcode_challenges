#-------------------------------------------------------------------------------
#    Valid Palindrome
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/valid-palindrome/
# Completed 4/28/19
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

''' Approach
1 Clean string with regex
    * Remove all special characters and white spaces
    * lower all letters
    * return a-z0-9
2 Split out the first half of the string
3 Split out the second half and reverse that string
    * Note steps 2 and 3 will ignore the middle number if string length is odd
4 Return first half == reversed second half
'''

#-------------------------------------------------------------------------------
#    Solution   
#-------------------------------------------------------------------------------

import re

class Solution:
    def isPalindrome(self, input_string: str) -> bool:
        """Test if input string is a palindrome. Ignores all white spaces and special characters

        Input:
        :input_string: str

        Output:
        True if input_string is a palindrome
        """
        cleaned_string = self.clean_string(input_string)
        if len(cleaned_string) == 1: return True
        return self.first_half(cleaned_string) == self.reverse_second_half(cleaned_string)

    def clean_string(self, input_string: str) -> str:
        """Remove all special characters and white spaces and lowers all characters"""
        characters = re.findall('[a-z0-9]+', input_string.lower())
        return ''.join(characters)

    def first_half(self, input_string: str) -> str:
        """Return first half of input string"""
        return input_string[: len(input_string) // 2]

    def reverse_second_half(self, input_string: str) -> str:
        """Return reversed second half of input string"""
        return input_string[- (len(input_string) // 2) :][::-1]

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_clean_string_converts_to_lowercase(self):
        self.assertEqual(Solution().clean_string('ABC'), 'abc')
    def test_clean_string_keeps_numbers(self):
        self.assertEqual(Solution().clean_string('123'), '123')
    def test_clean_string_removes_special_char(self):
        self.assertEqual(Solution().clean_string('abc!@#$%^&*()123'), 'abc123')

    def test_first_half_even(self):
        self.assertEqual(Solution().first_half('abcd'), 'ab')
    def test_first_half_odd(self):
        self.assertEqual(Solution().first_half('abcde'), 'ab')

    def test_reverse_second_half_even(self):
        self.assertEqual(Solution().reverse_second_half('abcd'), 'dc')
    def test_reverse_second_half_odd(self):
        self.assertEqual(Solution().reverse_second_half('abcde'), 'ed')

    def test_isPalindrome_abba(self):
        self.assertTrue(Solution().isPalindrome('abba'))
    def test_isPalindrome_abcba(self):
        self.assertTrue(Solution().isPalindrome('abcba'))
    def test_isPalindrome_abc(self):
        self.assertFalse(Solution().isPalindrome('abc'))
    def test_isPalindrome_everything(self):
        self.assertTrue(Solution().isPalindrome('12aBcD#$%^dC !ba ?21'))
    def test_isPalindrome_1(self):
        self.assertTrue(Solution().isPalindrome('1'))
        
unittest.main()
