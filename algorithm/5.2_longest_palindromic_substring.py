#-------------------------------------------------------------------------------
#    Longest Palindromic Substring
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/longest-palindromic-substring/
# Completed 6/5/19
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Scan the string.
2. Look for palindrome that is one or two units longer than previously found.
3. When found, expand around palindrome until new max is established.
4. Return longest found when length from pointer to end is shorter than longest
    found palindrome.
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

class LongestPalindrome:
    def __init__(self, string: str):
        self.string = string
        self.left = 0
        self.right = 0
        self.max_length_found = 0
        
    def is_palindrome(self, left: int, right: int) -> bool:
        """Return True if sub_string is a palindrome."""
        print(self.string, left, right)
        if self.string[left] == self.string[right - 1]:
            mid = (left + right) // 2
            r_mid = mid + (left + right)%2
            return self.string[left:mid] == self.string[r_mid:right][::-1]
        return False
            

    def check(self, right: int):
        """Return true if right pointer is in index range."""
        return right <= len(self.string)

    def stop_checking(self, left: int):
        """Return True if the remiaining string to check is shorter thaan the
        longest palindrome on record.
        """
        return left + self.max_length_found >= len(self.string)

    def update_max_length(self, left: int, right: int) -> 'self':
        """Update index pointers for new max palindrome."""
        self.left = left
        self.right = right
        self.max_length_found = right - left
    
    def solve(self) -> str:
        """Return the longest palindrome in the string."""
        print("\n\n")

        def _solve(left: int, right: int):
            if left < 0:
                _solve(left + 1, right + 1)
                return
            elif self.stop_checking(left):
                return 

            if self.check(right + 1):
                if self.is_palindrome(left, right + 1):
                    self.update_max_length(left, right + 1)
                    _solve(left - 1, right + 1)
                    return
                
            if self.check(right):
                if self.is_palindrome(left, right):
                    self.update_max_length(left, right)
                    _solve(left - 1, right)
                    return
                
            _solve(left + 1, right + 1)

        _solve(0, 0)
        return self.string[self.left:self.right]
    
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
        self.assertTrue(LongestPalindrome('a').is_palindrome(0,1))
    def test_is_palindrome_aa_True(self):
        self.assertTrue(LongestPalindrome('aa').is_palindrome(0,2))
    def test_is_palindrome_aba_True(self):
        self.assertTrue(LongestPalindrome('aba').is_palindrome(0,3))
    def test_is_palindrome_abba_True(self):
        self.assertTrue(LongestPalindrome('abba').is_palindrome(0,4))
    def test_is_palindrome_abba_bb_True(self):
        self.assertTrue(LongestPalindrome('abba').is_palindrome(1,3))
        
    def test_is_palindrome_ab_False(self):
        self.assertFalse(LongestPalindrome('ab').is_palindrome(0,2))
    def test_is_palindrome_abb_False(self):
        self.assertFalse(LongestPalindrome('abb').is_palindrome(0,3))
    def test_is_palindrome_abc_False(self):
        self.assertFalse(LongestPalindrome('abc').is_palindrome(0,3))
        

class TestSolution(unittest.TestCase):

    def test_empty(self):
        string = ''
        ans = ''
        self.assertEqual(Solution().longestPalindrome(string), ans)
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
    def test_odd_odd(self):
        string = 'CBBBDEFFFFFFG'
        ans = 'FFFFFF'
        self.assertEqual(Solution().longestPalindrome(string), ans)
    def test_aaaaaaaaaaaaaaaaaa(self):
        string = 'aaaaaaaaaaaaaaaaaaaa'
        ans = string
        self.assertEqual(Solution().longestPalindrome(string), ans)        
        
unittest.main()
