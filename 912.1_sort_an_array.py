# Sort an Array
# https://leetcode.com/problems/sort-an-array/
# Completed 4/25/19 With time out on large input test case
# Bubble Sort 

def bubble_sort(nums):
    unsorted = True
    while unsorted:
        unsorted = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                unsorted = True
                nums[i], nums[i - 1] = nums[i - 1], nums[i]

    return nums    

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return bubble_sort(nums)
