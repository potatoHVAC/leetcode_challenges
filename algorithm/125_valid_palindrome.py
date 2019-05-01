# Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# Completed 4/28/19

import re

class Solution:
    def isPalindrome(self, input_string: str) -> bool:
        # Return True if cleaned string is a palindrome
        cleaned_string = self.clean_string(input_string)
        if len(cleaned_string) == 1: return True
        return self.first_half(cleaned_string) == self.reverse_second_half(cleaned_string)

    def clean_string(self, input_string: str) -> str:
        # Remove all lowers all characters and remove all whitespaces and puncuation. 
        characters = re.findall('[a-z0-9]+', input_string.lower())
        return ''.join(characters)

    def first_half(self, input_string: str) -> str:
        return input_string[: len(input_string) // 2]

    def reverse_second_half(self, input_string: str) -> str:
        return input_string[- (len(input_string) // 2) :][::-1]
