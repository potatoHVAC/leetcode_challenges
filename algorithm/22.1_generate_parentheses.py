#-------------------------------------------------------------------------------
#    Generate Parentheses
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/generate-parentheses/
# Completed 7/6/19
#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def generate_parentheses(n: int):
    def _generate_parentheses(n: int, open_count: int, string: str, ans: list):
        if n == 0 and open_count == 0:
            ans.append(string)
        if open_count > 0:
            _generate_parentheses(n, open_count - 1, string + ")", ans)
        if n > 0:
            _generate_parentheses(n -  1, open_count + 1, string + "(", ans)
        return ans

    return _generate_parentheses(n, 0, "", [])

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        return generate_parentheses(n)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_3(self):
        n = 3
        ans = set(["()()()","()(())","(())()","(()())","((()))"])
        self.assertEqual(ans, set(Solution().generateParenthesis(n)))
    def test_0(self):
        n = 0
        ans = set([""])
        self.assertEqual(ans, set(Solution().generateParenthesis(n)))
    def test_1(self):
        n = 1
        ans = set(["()"])
        self.assertEqual(ans, set(Solution().generateParenthesis(n)))
    def test_2(self):
        n = 2
        ans = set(["(())","()()"])
        self.assertEqual(ans, set(Solution().generateParenthesis(n)))

unittest.main()
