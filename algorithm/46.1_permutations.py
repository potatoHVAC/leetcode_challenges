#-------------------------------------------------------------------------------
#    Permutations
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/permutations/
# 
#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def permute(nums: [int]) -> [[int]]:

    ans = []
    def _permute(nums: [int], path: [int]) -> [[int]]:
        if not nums:
            ans.append(path)
        else:
            for i, num in enumerate(nums):
                _permute(nums[:i]+nums[i+1:], [num] + path)

    _permute(nums, [])
    return ans

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        return permute(nums)
