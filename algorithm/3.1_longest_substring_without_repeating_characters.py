# Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#

from collections import defaultdict

class Solution:

    def __init__(self):
        self.head = 0
        self.tail = 0
        self.max_length_found = 0
        self.current_length = 0

        self.memory = defaultdict(int)

    def advance_tail(self, string: str) -> 'self':
        self.memory[string[self.tail]] -= 1
        self.current_length -= 1
        self.tail += 1
        
    def lengthOfLongestSubstring(self, string: str) -> int:
        while self.head < len(string):
            self.memory[string[self.head]] += 1
            self.current_length += 1

            while self.memory[string[self.head]] == 2:
                self.advance_tail(string)
                
            self.max_length_found = max(self.current_length, self.max_length_found)
            self.head += 1

        return self.max_length_found

#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_advance_tail_will_remove_letter(self):
        tst = Solution()
        tst.memory = {'a': 2}
        tst.advance_tail('a')
        self.assertEqual(tst.memory['a'], 1)
    def test_advance_tail_will_reduce_count_length(self):
        tst = Solution()
        tst.advance_tail('a')
        self.assertEqual(tst.current_length, -1)

    def test_lengthOfLongestSubstring_will_return_0_for_empty_string(self):
        string = ''
        self.assertEqual(Solution().lengthOfLongestSubstring(string), 0)        
    def test_lengthOfLongestSubstring_will_return_1_for_a(self):
        string = 'a'
        self.assertEqual(Solution().lengthOfLongestSubstring(string), 1)
    def test_lengthOfLongestSubstring_will_return_1_for_aa(self):
        string = 'aa'
        self.assertEqual(Solution().lengthOfLongestSubstring(string), 1)
    def test_lengthOfLongestSubstring_will_return_2_for_ab(self):
        string = 'ab'
        self.assertEqual(Solution().lengthOfLongestSubstring(string), 2)
    def test_lengthOfLongestSubstring_will_return_3_for_abcba(self):
        string = 'abcba'
        self.assertEqual(Solution().lengthOfLongestSubstring(string), 3)
    def test_lengthOfLongestSubstring_will_return_2_for_bba(self):
        string = 'bba'
        self.assertEqual(Solution().lengthOfLongestSubstring(string), 2)
    def test_lengthOfLongestSubstring_hackerrank_ex_1(self):
        string = 'abcabcbb'
        self.assertEqual(Solution().lengthOfLongestSubstring(string), 3)
    def test_lengthOfLongestSubstring_hackerrank_ex_3(self):
        string = 'pwwkew'
        self.assertEqual(Solution().lengthOfLongestSubstring(string), 3)

        
unittest.main()
