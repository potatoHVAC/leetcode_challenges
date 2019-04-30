# Target Sum
# https://leetcode.com/problems/target-sum/
# Almost Completed 4/29/19
# Valid solution but times out for large inputs. 

class Solution:
    def findTargetSumWays(self, nums: [int], target: int, num_sum: int = 0, pointer: int = 0) -> int:
        if self.target_not_in_range(nums, target, num_sum, pointer):
            return 0
        if pointer == len(nums) and num_sum == target:
            return 1

        return sum([
            self.findTargetSumWays(nums, target, num_sum + nums[pointer], pointer + 1),
            self.findTargetSumWays(nums, target, num_sum - nums[pointer], pointer + 1)
        ])
                
    def target_not_in_range(self, nums: [int], target: int, num_sum: int, pointer: int):
        remaining_sum = sum(nums[pointer:])
        range_min = num_sum - remaining_sum
        range_max = num_sum + remaining_sum + 1
        return target not in range(range_min, range_max)


