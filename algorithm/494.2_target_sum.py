# Target Sum
# https://leetcode.com/problems/target-sum/
# Completed 4/30/19

class Solution:
    def __init__(self):
        self.counts = {0: 1}
    
    def ingest_numbers(self, numbers: [int]):
        for number in numbers: self.update_sum_counter(number)
        return self

    def update_sum_counter(self, number: int):
        # Create new counter dictionary with all counts updated by +- number
        new_counts = {}
        for num_key, count in self.counts.items():
            try: new_counts[num_key + number] += count
            except: new_counts[num_key + number] = count
            try: new_counts[num_key - number] += count
            except: new_counts[num_key - number] = count
            
        self.counts = new_counts
        return self

    def get_target_count(self, target: int) -> int:
        # Return the number of ways to make the target with the given numbers
        if target in self.counts: return self.counts[target]
        return 0

    def findTargetSumWays(self, numbers: [int], target: int) -> int:
        return self.ingest_numbers(numbers).get_target_count(target)

#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_findTargetSumWays_1(self):
        nums = [1]
        target = 1
        answer = 1
        self.assertEqual(Solution().findTargetSumWays(nums, target), answer)
    def test_findTargetSumWays_1_negative(self):
        nums = [1]
        target = -1
        answer = 1
        self.assertEqual(Solution().findTargetSumWays(nums, target), answer)
    def test_findTargetSumWays_2(self):
        nums = [1, 1]
        target = 0
        answer = 2
        self.assertEqual(Solution().findTargetSumWays(nums, target), answer)
    def test_findTargetSumWays_3(self):
        nums = [1, 1, 1, 1, 1]
        target = 3
        answer = 5
        self.assertEqual(Solution().findTargetSumWays(nums, target), answer)
    def test_findTargetSumWays_4(self):
        nums = [1, 2, 3]
        target = 0
        answer = 2
        self.assertEqual(Solution().findTargetSumWays(nums, target), answer)

unittest.main()
