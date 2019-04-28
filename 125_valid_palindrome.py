# Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# Completed 4/28/19

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = self.clean_string(s)
        if len(cleaned_string) == 1: return True
        return self.first_half(cleaned_string) == self.reverse_second_half(cleaned_string)

    def clean_string(self, input_string):
        characters = re.findall('[a-z0-9]+', input_string.lower())
        return ''.join(characters)

    def first_half(self, string):
        return string[: len(string) // 2]

    def reverse_second_half(self, string):
        return string[- (len(string) // 2) :][::-1]
