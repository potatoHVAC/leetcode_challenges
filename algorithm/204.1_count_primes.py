# Count Primes
# https://leetcode.com/problems/count-primes/
# Completed 4/28/19

class Solution:
    def countPrimes(self, number: int) -> int:
        """Count the number of primes below the target integer.

        Input:
        :number: int -- check all numbers below target

        Output:
        int -- number of primes below :number:
        """
        if number < 2: return 0

        primes_bool = [False] * 2 + [True] * (number - 2)

        for i in range(2, number):
            if primes_bool[i]:
                target = i * 2
                while target < number:
                    primes_bool[target] = False
                    target += i

        return sum(primes_bool)

#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_countPrimes_1(self):
        self.assertEqual(Solution().countPrimes(1), 0)
    def test_countPrimes_2(self):
        self.assertEqual(Solution().countPrimes(2), 0)
    def test_countPrimes_0(self):
        self.assertEqual(Solution().countPrimes(0), 0)
    def test_countPrimes_10(self):
        self.assertEqual(Solution().countPrimes(10), 4)
    def test_countPrimes_1(self):
        self.assertEqual(Solution().countPrimes(100), 25)        
        
unittest.main()
