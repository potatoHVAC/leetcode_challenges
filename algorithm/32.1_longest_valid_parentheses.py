#-------------------------------------------------------------------------------
#    Longest Valid Parentheses
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/longest-valid-parentheses/
# Completed 6/10/19
#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

class ValidParentheses:

    def __init__(self, string: str):
        self.string = string
        self.ans = self._solve()

    def _analyze_str(self, string):
        """Convert :string: into ( = 1 and ) = -1."""

        def _to_int(char: str) -> int:
            if char == '(':
                return 1
            return -1
        
        return list(map(_to_int, [ char for char in string ]))
        
    def _check(self, string):
        """Return Longest found valid set of parenthenses.
        Note: this is not guarinteed to be max longest until the reversed 
        string is checked.
        """
        stats = self._analyze_str(string)
        
        last_sum = -1
        start_index = None
        longest = (0,0)
        for i, num in enumerate(stats):
            if last_sum == -1:
                new_sum = num
            else:
                new_sum = last_sum + num
            
            if new_sum == 1 and last_sum == -1:
                start_index = i
            if new_sum == 0 and i-start_index > longest[1]-longest[0]:
                longest = (start_index, i + 1)
            last_sum = new_sum

        return string[longest[0]:longest[1]]

    def _reverse(self, string):
        """Reverse the parentheses string."""
        if len(string) == 0:
            return string

        def _opposite(char: str) -> str:
            if char == '(':
                return ')'
            return '('

        return ''.join(map(_opposite, ''.join(reversed(string))))

    def _check_reversed(self, string):
        """Reverse the string and feed it inot _check then reverse the output."""
        reverse_str = self._reverse(string)
        checked = self._check(reverse_str)
        return self._reverse(checked)

    def _solve(self):
        """Return length of the longest valid substring of parentheses."""
        forward = self._check(self.string)
        backward = self._check_reversed(self.string)

        return max(len(forward), len(backward))

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """Return length of the longest valid substring of parentheses.

        Input:
        :s: str -> string of parentheses

        Output:
        int -> length of longest substring of parentheses
        """
        return ValidParentheses(s).ans

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_1(self):
        string = '()'
        ans = 2
        self.assertEqual(Solution().longestValidParentheses(string), ans)
    def test_2(self):
        string = '('
        ans = 0
        self.assertEqual(Solution().longestValidParentheses(string), ans)
    def test_3(self):
        string = ')'
        ans = 0
        self.assertEqual(Solution().longestValidParentheses(string), ans)
    def test_4(self):
        string = ')()'
        ans = 2
        self.assertEqual(Solution().longestValidParentheses(string), ans)
    def test_5(self):
        string = ')))'
        ans = 0
        self.assertEqual(Solution().longestValidParentheses(string), ans)
    def test_6(self):
        string = ')()))()()('
        ans = 4
        self.assertEqual(Solution().longestValidParentheses(string), ans)
    def test_7(self):
        string = ')()())'
        ans = 4
        self.assertEqual(Solution().longestValidParentheses(string), ans)
    def test_8(self):
        string = '(()'
        ans = 2
        self.assertEqual(Solution().longestValidParentheses(string), ans)
    def test_9(self):
        string = ')()))))(((()()(('
        ans = 4
        self.assertEqual(Solution().longestValidParentheses(string), ans)
    def test_10(self):
        string = ')(((())))'
        ans = 8
        self.assertEqual(Solution().longestValidParentheses(string), ans)
    def test_11(self):
        string = ')()))))))))))))))('
        ans = 2
        self.assertEqual(Solution().longestValidParentheses(string), ans)

unittest.main()
