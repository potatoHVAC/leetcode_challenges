# Count Primes
# https://leetcode.com/problems/count-primes/
# Completed 4/28/19

class Solution:
    def countPrimes(self, number: int) -> int:
        if number < 2: return 0

        primes_bool = [False] * 2 + [True] * (number - 2)

        for i in range(2, number):
            if primes_bool[i]:
                target = i * 2
                while target < number:
                    primes_bool[target] = False
                    target += i

        return sum(primes_bool)
