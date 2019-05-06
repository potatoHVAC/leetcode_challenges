# Sum of Even Numbers After Queries
# https://leetcode.com/problems/sum-of-even-numbers-after-queries/
# Completed 5/6/19

def is_even(num: int) -> bool:
    # Return True if input is even number
    return num%2 == 0
    
class Solution:
    def sumEvenAfterQueries(self, ints: [int], queries: [[int]]) -> [int]:
        results = []
        even_sum = sum([ num for num in ints if is_even(num)])
        for querie in queries:
            i = querie[1]
            if is_even(ints[i]): even_sum -= ints[i]
            
            ints[i] += querie[0]
            if is_even(ints[i]): even_sum += ints[i]
            results.append(even_sum)
        return results
    
