#-------------------------------------------------------------------------------
#    Letter Combinations of a Phone Number
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Completed 6/13/19
#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

class Combinations:

    def __init__(self, digits: str):
        self.digits = digits
        self.ans = self._solve()

    def _solve(self):
        if self.digits == "":
            return []

        key = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6":"mno",
               "7":"pqrs", "8":"tuv", "9":"wxyz"}
        def __solve(digits: str):
            if not digits:
                return [""]

            ans = []
            next_ans = __solve(digits[1:])
            for c in key[digits[0]]:
                for string in next_ans:
                    ans.append(c + string)
                    
            return ans

        return __solve(self.digits)

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        """Return list of all possible character combinations for phone number.

        Input:
        :digits: str -> phone number

        Output:
        [str] -> list of all combinations
        """
        return Combinations(digits).ans

