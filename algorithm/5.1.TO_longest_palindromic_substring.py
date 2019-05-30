#-------------------------------------------------------------------------------
#    Longest Palindromic Substring
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/longest-palindromic-substring/
# Almost Completed 5/28/19
# Time out for large inputs
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Dynamic Programming
 1.1 Return charicter if string length is 1.
 1.2 Check if current string is a palindrome.
     * Record string if palindrome.
 1.3 Check both possible smaller strings.
     * String with last character removed.
     * String with first character removed.
     * Record string with max length of previous two steps.
       (prioratize first option if length is the same)
 1.4 Return memoize[string]
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

class LongestPalindrome:
    def __init__(self, string: str):
        self.string = string

    def is_palindrome(self, sub_string: str) -> bool:
        """Return True if :sub_string: is a palindrome"""
        mid = len(sub_string) // 2

        if len(sub_string) == 1:
            return True
        return sub_string[:mid] == sub_string[-mid:][::-1]

    def solve(self):
        """Dynamically find longest palindromic substring"""

        memoize_sub_strings = {}
        def _solve(sub_string: str) -> str:
            if len(sub_string) == 1:
                return sub_string

            if sub_string not in memoize_sub_strings:
                if self.is_palindrome(sub_string):
                    memoize_sub_strings[sub_string] = sub_string
                else:
                    remove_last = _solve(sub_string[:-1])
                    remove_first = _solve(sub_string[1:])
                    
                    if len(remove_first) > len(remove_last):
                        memoize_sub_strings[sub_string] = remove_first
                    else:
                        memoize_sub_strings[sub_string] = remove_last
            return memoize_sub_strings[sub_string]

        return _solve(self.string)
    
#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def longestPalindrome(self, string: str) -> str:
        """Find longest palindrome substring

        Input:
        :string: str -> input string

        Output:
        str -> longest palindrome substring
        """
        return LongestPalindrome(string).solve()

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestLongestPalindrome(unittest.TestCase):

    def test_is_palindrome_a_True(self):
        self.assertTrue(LongestPalindrome('a').is_palindrome('a'))
    def test_is_palindrome_aa_True(self):
        self.assertTrue(LongestPalindrome('a').is_palindrome('aa'))
    def test_is_palindrome_aba_True(self):
        self.assertTrue(LongestPalindrome('a').is_palindrome('aba'))
    def test_is_palindrome_abba_True(self):
        self.assertTrue(LongestPalindrome('a').is_palindrome('abba'))

    def test_is_palindrome_ab_True(self):
        self.assertFalse(LongestPalindrome('a').is_palindrome('ab'))
    def test_is_palindrome_abb_True(self):
        self.assertFalse(LongestPalindrome('a').is_palindrome('abb'))
    def test_is_palindrome_abc_True(self):
        self.assertFalse(LongestPalindrome('a').is_palindrome('abc'))
        

class TestSolution(unittest.TestCase):

    def test_A(self):
        string = 'A'
        ans = 'A'
        self.assertEqual(Solution().longestPalindrome(string), ans)
    def test_AB(self):
        string = 'AB'
        ans = 'A'
        self.assertEqual(Solution().longestPalindrome(string), ans)
    def test_ABA(self):
        string = 'ABA'
        ans = 'ABA'
        self.assertEqual(Solution().longestPalindrome(string), ans)
    def test_BABAD(self):
        string = 'BABAD'
        ans = 'BAB'
        self.assertEqual(Solution().longestPalindrome(string), ans)
    def test_CBBD(self):
        string = 'CBBD'
        ans = 'BB'
        self.assertEqual(Solution().longestPalindrome(string), ans)
    def test_CBBDEFFFG(self):
        string = 'CBBDEFFFG'
        ans = 'FFF'
        self.assertEqual(Solution().longestPalindrome(string), ans)
        
unittest.main()
