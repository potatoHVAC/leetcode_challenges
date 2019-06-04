#-------------------------------------------------------------------------------
#    Longest Word in Dictionary
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/longest-word-in-dictionary/
# Completed 6/4/19
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Create Trie class
2. Insert each word into Trie recording when words end.
3. Dynamic DFS Traverse Trie and return longest word.
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

class TrieNode:

    def __init__(self, chars: str):
        self.chars = chars
        self.children = {}
        self.end = False
        
class Trie:

    def __init__(self):
        self.head = TrieNode('')
        self.head.end = True

    def insert(self, word: str) -> 'self':
        """Insert word into Trie"""

        def _insert(node: TrieNode, word: str, size: int):
            trie_key = word[:size]

            if trie_key not in node.children:
                node.children[trie_key] = TrieNode(trie_key)

            if trie_key == word:
                node.children[trie_key].end = True
                return
            
            _insert(node.children[trie_key], word, size + 1)

        _insert(self.head, word, 1)
        
        return self

    def insert_words(self, words: [str]) -> 'self':
        """Insert list of words into Trie"""
        for word in words:
            self.insert(word)
        return self

    def longest_word(self) -> str:
        """Return longest word comprised of smaller words"""

        memoize = {}
        def _longest_word(node: TrieNode) -> str:
            if not node.end:
                return ""
            
            if node.chars not in memoize:
                word = node.chars
                for next_word, child_node in node.children.items():
                    next_word = _longest_word(child_node)
                    if len(next_word) > len(word):
                        word = next_word
                    elif len(next_word) >= len(word) and next_word < word:
                        word = next_word

                memoize[node.chars] = word

            return memoize[node.chars]

        return _longest_word(self.head)

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def longestWord(self, words: [str]) -> str:
        """Return the longest word made of sub words

        Input:
        :words: [str] -> list of dictionary words

        Output:
        str -> longest word
        """
        return Trie().insert_words(words).longest_word()

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_empty(self):
        words = []
        ans = ""
        self.assertEqual(Solution().longestWord(words), ans)
    def test_a(self):
        words = ["a"]
        ans = "a"
        self.assertEqual(Solution().longestWord(words), ans)
    def test_none(self):
        words = ["aa"]
        ans = ""
        self.assertEqual(Solution().longestWord(words), ans)
    def test_shorter_of_same_length1(self):
        words = ["b", "a"]
        ans = "a"
        self.assertEqual(Solution().longestWord(words), ans)
    def test_skip_dead_ends(self):
        words = ["b", "bb", "aaa", "a"]
        ans = "bb"
        self.assertEqual(Solution().longestWord(words), ans)
    def test_shorter_of_same_length2(self):
        words = ["a", "b", "bb", "aa"]
        ans = "aa"
        self.assertEqual(Solution().longestWord(words), ans)
    def test_ex1(self):
        words = ["w","wo","wor","worl", "world"]
        ans = "world"
        self.assertEqual(Solution().longestWord(words), ans)
    def test_ex2(self):
        words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
        ans = "apple"
        self.assertEqual(Solution().longestWord(words), ans)
    def test_long(self):
        words = ["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh"]
        ans = "abcdefgh"
        self.assertEqual(Solution().longestWord(words), ans)        
        
unittest.main()

