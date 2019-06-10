#-------------------------------------------------------------------------------
#    Substring with Concatenation of All Words
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# Completed 6/8/19
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Create Counter of all input words.
2. Iterate over string selecting all substrings with length of concatenated words.
 2.1 Seperate each substring into chunks of length of each word.
 2.2 Create Counter of chunks
 2.3 If this Counter == words Counter then append index to answer
3. Return answer
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

from collections import Counter

class Concat:

    def __init__(self, string: str, words: [str]):
        self.string = string
        self.words = words
        self.words_count = Counter(words)
        self.ans = []
        self._solve()

    def _check(self, substring: str) -> bool:
        """Return True if substring made up of all words."""
        word_len = len(self.words[0])
        sub_words_count = Counter([
            substring[i*word_len:(i+1)*word_len] for i in range(len(self.words))
        ])
        return sub_words_count == self.words_count
        
    def _solve(self) -> None:
        """Append starting index(s) to :self.ans:"""
        if not self.words:
            return

        def __solve(left: int, right: int) -> None:
            if right < len(self.string):
                if self._check(self.string[left:right+1]):
                    self.ans.append(left)
                __solve(left + 1, right + 1)

        __solve(0, len("".join(self.words)) - 1)
                

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def findSubstring(self, s: str, words: [str]) -> [int]:
        """Return starting index of concatenated substrings.

        Input:
        :s:     str   -> target string
        :words: [str] -> words to concatenate

        Output:
        [int] -> list of starting index(s)
        """
        return Concat(s, words).ans

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_abc1(self):
        string = 'abc'
        words = ['a', 'b']
        ans = [0]
        self.assertEqual(Solution().findSubstring(string, words), ans)
    def test_abc2(self):
        string = 'abc'
        words = ['c', 'b']
        ans = [1]
        self.assertEqual(Solution().findSubstring(string, words), ans)
    def test_ex1(self):
        string = "barfoothefoobarman"
        words = ["foo","bar"]
        ans = [0,9]
        self.assertEqual(Solution().findSubstring(string, words), ans)
    def test_ex2(self):
        string = "wordgoodgoodgoodbestword"
        words = ["word","good","best","word"]
        ans = []
        self.assertEqual(Solution().findSubstring(string, words), ans)
    def test_empty_words(self):
        string = 'abc'
        words = []
        ans = []
        self.assertEqual(Solution().findSubstring(string, words), ans)
    def test_empty_string(self):
        string = ''
        words = ['a', 'b']
        ans = []
        self.assertEqual(Solution().findSubstring(string, words), ans)
        
unittest.main()
