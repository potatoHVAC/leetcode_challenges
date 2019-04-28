# Count Primes
# https://leetcode.com/problems/count-primes/
# Completed 4/28/19


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0

        primes_bool = [False] * 2 + [True] * (n - 2)

        for i in range(2, n):
            if primes_bool[i]:
                target = i * 2
                while target < n:
                    primes_bool[target] = False
                    target += i

        return sum(primes_bool)
