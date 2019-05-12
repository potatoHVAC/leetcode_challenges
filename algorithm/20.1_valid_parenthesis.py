# Valid Parenthesis
# https://leetcode.com/problems/valid-parentheses/
# Completed 5/12/19

import re

class Solution:
    def isValid(self, sequence: str) -> bool:
        # Return True if sequence is empty
        #        False if nothing removed from sequence
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
