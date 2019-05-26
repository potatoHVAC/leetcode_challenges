#-------------------------------------------------------------------------------
#    3Sum
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/3sum/
# Almost Completed 5/24/19
# O(n**3) times out with large inputs
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Create dictionary :memoize1: where key is an element of :nums: and value is
    a list containing the index of that element. This will be a list of lists
    to handle duplicate entries.
2. Create dictionary :memoize2: 
 2.1 Scan :memoize1: and sum each key with each element of :nums:
 2.2 Append the element index to each list in :memoize1: (assuming index is not
      already stored in that list). Creating a new set of [[indices]] of two
      elements from :nums: whos sum is :memoize2: key.
3. Repeate step 2 making :memoize3: which contains triplets of indices whos 
    elements of :nums: sum to the dictionary keys.
4. Return :memoize3:[0] with the indices replaced with their elements and sorted
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

from collections import defaultdict
from pprint import pprint

class ThreeSum:
    def __init__(self, nums: [int]):
        self.nums = nums

    def _to_sorted_str(self, nums: [int]) -> str:
        """Sort list and format as ',' seperated string"""
        sorted_nums = sorted(nums)
        return ",".join(map(str, sorted_nums))

    def _to_list(self, nums_string: str) -> [int]:
        """Convert ',' seperated string into list of int"""
        if nums_string == "":
            return []
        return list(map(int, nums_string.split(",")))

    def _format_ans(self, nums_strings: str) -> [[int]]:
        """Convert all solution strings into list of list[int]"""
        return list(map(self._to_list, nums_strings))

    def _add_element_to_str(self, nums_string: str, element: int) -> str:
        """Return ',' seperated string with element added in sorted order"""
        nums = self._to_list(nums_string)
        nums.append(element)
        return self._to_sorted_str(nums)
        
    def solve(self):

        def _memoize(old_memoize: defaultdict) -> defaultdict:
            """Increase elements of memoize with all elements of self.nums"""
            new_memoize = defaultdict(dict)
            for key_sum, nums_dict in old_memoize.items():
                for nums_key, indices in nums_dict.items():
                    for index, element in enumerate(self.nums):
                        new_key_sum = key_sum + element

                        if index not in indices:
                            new_set = indices | set([index])
                            new_nums_key = self._add_element_to_str(nums_key, element)
                            new_memoize[new_key_sum][new_nums_key] = new_set.copy()

            return new_memoize

        memoize0 = {0:{'': set()}}
        memoize3 = _memoize(_memoize(_memoize(memoize0)))
        return self._format_ans(memoize3[0])

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        """Solve 3sum

        Input:
        :nums: [int] -> list of integers

        Output:
        [[int]] -> 2D list of ints representing all tripplets that sum to zero"""
        return ThreeSum(nums).solve()

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_simple(self):
        nums = [1, 0 , -1]
        ans = [[-1, 0, 1]]
        self.assertEqual(Solution().threeSum(nums), ans)
    def test_double(self):
        nums = [1, 0, 1, -1]
        ans = [[-1, 0, 1]]
        self.assertEqual(Solution().threeSum(nums), ans)
    def test_none(self):
        nums = [1, 0, 1]
        ans = []
        self.assertEqual(Solution().threeSum(nums), ans)
    def test_double_in_output(self):
        nums = [2, -1, -1]
        ans = [[-1, -1, 2]]
        self.assertEqual(Solution().threeSum(nums), ans)
    def test_example1(self):
        nums = [-1, 0, 1, 2, -1, -4]
        ans = [[-1,0,1],[-1,-1,2]]
        solve = Solution().threeSum(nums)
        self.assertTrue(ans[0] in solve and ans[1] in solve)

unittest.main()
