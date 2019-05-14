# Wildcard Matching
# https://leetcode.com/problems/wildcard-matching/
# Completed 5/13

class Solution:
    def isMatch(self, string: str, pattern: str) -> bool:
        """Check if pattern is an exact match to string

        Input: 
        :string:  str -- the string to match
        :pattern: str -- the pattern to match with string
        
        Output:
        True -- if pattern matches string
        """
        clean_pattern = self.pattern_cleaner(pattern)
        if string == '' and clean_pattern == '*':
            return True

        memoize = {str(len(string)) + '.' + str(len(clean_pattern)): True}
        def _isMatch(string: str, s_pointer: int, pattern: str, p_pointer: int) -> bool:
            """Solve isMatch with dynamic programing"""
            key = str(s_pointer) + '.' + str(p_pointer)

            if key not in memoize:
                if p_pointer == len(pattern):
                    output = False
                elif s_pointer == len(string):
                    if p_pointer < len(pattern) and pattern[p_pointer] == '*':
                        output = _isMatch(string, s_pointer, pattern, p_pointer + 1)
                    else:
                        output = False
                        
                elif pattern[p_pointer] in ['?', string[s_pointer]]:
                    output = _isMatch(string, s_pointer + 1, pattern, p_pointer + 1)
                elif pattern[p_pointer] == '*':
                    advance_string = _isMatch(string, s_pointer + 1, pattern, p_pointer)
                    advance_pattern = _isMatch(string, s_pointer, pattern, p_pointer + 1)
                    advance_both = _isMatch(string, s_pointer + 1, pattern, p_pointer + 1)
                    output = advance_string or advance_pattern or advance_both
                else:
                    output = False
                memoize[key] = output

            return memoize[key]
        return _isMatch(string, 0, clean_pattern, 0)

    def pattern_cleaner(self, pattern: str) -> str:
        """Remove duplicate wild cards ('*') from pattern"""
        if len(pattern) == 0:
            return pattern
        
        clean_pattern = pattern[0]
        for c in pattern[1:]:
            if c == '*' and c == clean_pattern[-1]:
                pass
            else:
                clean_pattern += c
            
        return clean_pattern

#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_isMatch_a_a(self):
        self.assertTrue(Solution().isMatch('a', 'a'))
    def test_isMatch_aa_a(self):
        self.assertFalse(Solution().isMatch('aa', 'a'))
    def test_isMatch_a_wild(self):
        self.assertTrue(Solution().isMatch('a', '*'))
    def test_isMatch_ab_wild(self):
        self.assertTrue(Solution().isMatch('ab', '*'))
    def test_isMatch_a_question(self):
        self.assertTrue(Solution().isMatch('a', '?'))
    def test_isMatch_cb_question(self):
        self.assertTrue(Solution().isMatch('cb', '?b'))
    def test_isMatch_adceb_wild(self):
        self.assertTrue(Solution().isMatch('adceb', '*a*b'))
    def test_isMatch_acbcb_wild(self):
        self.assertFalse(Solution().isMatch('acbcb', 'a*c?b'))
    def test_isMatch_empty_wild(self):
        self.assertTrue(Solution().isMatch('', '*'))
    def test_isMatch_empty_wildwild(self):
        self.assertTrue(Solution().isMatch('', '**'))
    def test_isMatch_empty_empty(self):
        self.assertTrue(Solution().isMatch('', ''))
    def test_isMatch_a_awild(self):
        self.assertTrue(Solution().isMatch('a', 'a*'))
    def test_isMatch_a_questionwild(self):
        self.assertTrue(Solution().isMatch('a', '?*'))
    def test_isMatch_a_wildquestion(self):
        self.assertTrue(Solution().isMatch('a', '*?'))
    def test_isMatch_a_awildwilda(self):
        self.assertFalse(Solution().isMatch('a', 'a**a'))
    def test_isMatch_aa_awildwilda(self):
        self.assertTrue(Solution().isMatch('aa', 'a**a'))
        
unittest.main()    
