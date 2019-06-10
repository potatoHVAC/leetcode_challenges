#-------------------------------------------------------------------------------
#    Happy Number
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/happy-number/
# Completed 6/8/19
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Initialize set with input number.
2. Recursive function to find next number in sequence.
 2.1 Return False if new number is in set.
 2.2 Return True if next number is 1.
 2.3 Add new number to set.
 2.4 Call next number.
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def my_happy_function(num: int) -> bool:
    """Return True if number is happy."""

    def _my_happy_function(num: int, memoize: set) -> bool:
        next_num = sum([ int(n)**2 for n in str(num)])
        if next_num == 1:
            return True
        elif next_num in memoize:
            return False
        memoize.add(next_num)

        return _my_happy_function(next_num, memoize)

    return _my_happy_function(num, set([num]))

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def isHappy(self, n: int) -> bool:
        """Return True if number is happy.

        Input:
        :n: int -> target number
        
        Output:
        bool -> True if number is happy
        """
        return my_happy_function(n)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_1(self):
        self.assertTrue(Solution().isHappy(1))
    def test_2(self):
        self.assertFalse(Solution().isHappy(2))
    def test_3(self):
        self.assertFalse(Solution().isHappy(3))
    def test_4(self):
        self.assertFalse(Solution().isHappy(4))
    def test_5(self):
        self.assertFalse(Solution().isHappy(5))
    def test_6(self):
        self.assertFalse(Solution().isHappy(6))
    def test_7(self):
        self.assertTrue(Solution().isHappy(7))
    def test_8(self):
        self.assertFalse(Solution().isHappy(8))
    def test_9(self):
        self.assertFalse(Solution().isHappy(9))
    def test_10(self):
        self.assertTrue(Solution().isHappy(10))
    def test_19(self):
        self.assertTrue(Solution().isHappy(19))

unittest.main()
