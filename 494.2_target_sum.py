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
