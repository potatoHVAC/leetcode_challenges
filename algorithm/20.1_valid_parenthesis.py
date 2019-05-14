# Valid Parenthesis
# https://leetcode.com/problems/valid-parentheses/
# Completed 5/12/19

"""Approach
1. Use regex to replace all () [] {} sets with empty strings and save to 
   a new variable.
2. If new length == old length then check completion.
  2.1 Return True if new length == 0
  2.2 Return False if new length > 0
3. Repeat steps 1 and 2 until done.
"""

import re

class Solution:
    def isValid(self, sequence: str) -> bool:
        """Check if a sequence of () [] {} is valid.

        Input:
        :sequence: str -- only contains () {} []

        Output:
        True -- if sequence is valid
        """
        new_sequence = re.sub('({}|\(\)|\[\])', '', sequence)
        if len(sequence) == len(new_sequence):
            return len(sequence) == 0
        return self.isValid(new_sequence)

#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_isValid_one_set(self):
        self.assertTrue(Solution().isValid('{}'))
    def test_isValid_all_set(self):
        self.assertTrue(Solution().isValid('{}[]()'))
    def test_isValid_all_set2(self):
        self.assertTrue(Solution().isValid('{{}}[[]](())'))
    def test_isValid_nested(self):
        self.assertTrue(Solution().isValid('[{}[]()]'))

    def test_isValid_one(self):
        self.assertFalse(Solution().isValid(']'))
    def test_isValid_all_the_same(self):
        self.assertFalse(Solution().isValid('((('))
    def test_isValid_extra_left(self):
        self.assertFalse(Solution().isValid('){}())'))
    def test_isValid_extra_right(self):
        self.assertFalse(Solution().isValid('[][])'))

unittest.main()
