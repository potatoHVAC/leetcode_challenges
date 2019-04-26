# Sort an Array
# https://leetcode.com/problems/sort-an-array/
#
# Quick Sort
from random import randint

def quick_sort(nums):
    if not nums: return nums
    pivot = randint(0, len(nums) - 1)

    smaller = [ num for num in nums if num < nums[pivot] ]
    same = [ num for num in nums if num == nums[pivot] ]
    larger = [ num for num in nums if num > nums[pivot] ]
    return quick_sort(smaller) + same + quick_sort(larger) 
    
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return quick_sort(nums)
