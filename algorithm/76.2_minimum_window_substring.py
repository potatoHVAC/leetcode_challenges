#-------------------------------------------------------------------------------
#    Minimum Window Substring
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/minimum-window-substring/
# Almost Completed 6/11/19
# Recursion dpeth error
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Two pointer
2. Move right pointer until all letters in T.
3. Check length and update if shortest.
4. Move left pointer until sub_string is missing one character. 
5. Repeat 2 through 4 until out of string.
6. Return shortest or empty string if none.
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

from collections import Counter

def _contains_all(target: Counter, sub_count: Counter) -> bool:
    """"""
    for char, count in target.items():
        if sub_count[char] < count:
            return False
    return True
    
def min_window(string: str, target: str) -> str:
    """Return shortest sub string containing all :target: letters."""

    target_count = Counter([ c for c in target ])    
    sub_string_count = Counter()
    left = right = 0
    sub_string = ""
    
    while right < len(string) + 1:
        if _contains_all(target_count, sub_string_count):
            new_sub_string = string[left:right]
            if sub_string == "" or len(sub_string) > len(new_sub_string):
                sub_string = new_sub_string
                
            sub_string_count[string[left]] -= 1
            left += 1
        else:
            if right < len(string):
                sub_string_count[string[right]] += 1
            right += 1

    return sub_string

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """Return shortest sub string containing all :t: letters.

        Input:
        :s: str -> string to check
        :t: str -> characters for substring

        Output:
        str -> shortest sub string containing elements of :t:
        """        
        return min_window(s, t)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_a_a(self):
        string = 'a'
        target = 'a'
        ans = 'a'
        self.assertEqual(Solution().minWindow(string, target), ans)
    def test_abc_b(self):
        string = 'abc'
        target = 'b'
        ans = 'b'
        self.assertEqual(Solution().minWindow(string, target), ans)
    def test_abcbd_bb(self):
        string = 'abcbd'
        target = 'bb'
        ans = 'bcb'
        self.assertEqual(Solution().minWindow(string, target), ans)
    def test_shorter_after_first_match(self):
        string = 'abaaabcbd'
        target = 'bb'
        ans = 'bcb'
        self.assertEqual(Solution().minWindow(string, target), ans)
    def test_shorter_is_first_match(self):
        string = 'ababcccbd'
        target = 'bb'
        ans = 'bab'
        self.assertEqual(Solution().minWindow(string, target), ans)
    def test_ex1(self):
        string = 'ADOBECODEBANC'
        target = 'ABC'
        ans = 'BANC'
        self.assertEqual(Solution().minWindow(string, target), ans)
    def test_long(self):
        string = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        target = 'aaaa'
        ans = 'aaaa'
        self.assertEqual(Solution().minWindow(string, target), ans)
    def test_none1(self):
        string = 'aaaaaaaaaaa'
        target = 'b'
        ans = ''
        self.assertEqual(Solution().minWindow(string, target), ans)
    def test_none2(self):
        string = 'aaaaabaaaaaa'
        target = 'abb'
        ans = ''
        self.assertEqual(Solution().minWindow(string, target), ans)
    def test_none3(self):
        string = 'aaaaabaaaaaa'
        target = 'abc'
        ans = ''
        self.assertEqual(Solution().minWindow(string, target), ans)
        
unittest.main()

