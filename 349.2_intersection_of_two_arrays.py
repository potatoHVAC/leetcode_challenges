# Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/
# Completed 4/28/19

class Solution:
    def intersection(self, nums1: [int], nums2: [int]) -> [int]:
        return list(set(nums1) & set(nums2))
        
