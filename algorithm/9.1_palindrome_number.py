# Palindrome Number
# https://leetcode.com/problems/palindrome-number/
# Completed 5/9/19

class Solution:
    def isPalindrome(self, input_int: int) -> bool:
        return str(input_int) == self.reverse_str(str(input_int))

    def reverse_str(self, string: str) -> str:
        return "".join([ char for char in string ][::-1])

#-------------------------------------------------------------------------------

import unittest

class TestIsPalindrome(unittest.TestCase):

    def test_1(self):
        self.assertTrue(Solution().isPalindrome(4))
    def test_121(self):
        self.assertTrue(Solution().isPalindrome(121))
    def test_11(self):
        self.assertTrue(Solution().isPalindrome(11))
    def test_12(self):
        self.assertFalse(Solution().isPalindrome(12))
    def test_1221(self):
        self.assertTrue(Solution().isPalindrome(1221))        
    def test_negative(self):
        self.assertFalse(Solution().isPalindrome(-5))    

if __name__ == '__main__':
    unittest.main()
