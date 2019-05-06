# Reverse String
# https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1440/
# Completed 5/5/19

class Solution:
    def reverseString(self, s: [str], i: int = 0) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        swap_i = len(s) - (i + 1)
        if i < swap_i:
            s[i], s[swap_i] = s[swap_i], s[i]
            self.reverseString(s, i + 1)
