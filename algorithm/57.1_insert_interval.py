#-------------------------------------------------------------------------------
#    Insert Interval
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/insert-interval/
# Completed 6/11/19
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Iterate intervals.
2. If less than new interval, append to ans.
3. If overlapping, merge with new interval.
4. If greater than, return ans + new interval + remaining. 
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def _in_range(interval: [int], new_interval: [int]) -> bool:
    """Return True if :interval: and :new_interval: overlap."""
    if interval[1] < new_interval[0]:
        return False
    elif interval [0] > new_interval[1]:
        return False
    return True
        

def _combine(intervals: [[int]], new_interval: [int]) -> [[int]]:
    """Return combined overlapping intervals. Inputs must all overlap."""
    if not intervals:
        return [new_interval]
    return [[
        min(intervals[0][0], new_interval[0]),
        max(intervals[-1][1], new_interval[1])
    ]]

def interval_insert(intervals: [[int]], new_interval: [int]) -> [[int]]:
    """Return intervals with new_interval merged in order."""
    lower_ranges = [ itl for itl in intervals if new_interval[0] > itl[1] ]
    in_range = [ itl for itl in intervals if _in_range(itl, new_interval) ]
    higher_ranges = [ itl for itl in intervals if new_interval[1] < itl[0] ]

    combined_ranges = _combine(in_range, new_interval)

    return lower_ranges + combined_ranges + higher_ranges

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def insert(self, intervals: [[int]], newInterval: [int]) -> [[int]]:
        """Return :intervals: with :newInterval: inserted in order.

        Input:
        :intervals:   [[int]] -> sorted list of intervals
        :newInterval: [int]   -> interval to be inserted

        Output:
        [[int]] -> sorted list of intervals
        """
        return interval_insert(intervals, newInterval)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_simple(self):
        intervals = [[1,2], [5,6]]
        new_interval = [3,4]
        ans = [[1,2],[3,4],[5,6]]
        self.assertEqual(Solution().insert(intervals, new_interval), ans)
    def test_beginning(self):
        intervals = [[3,4], [5,6]]
        new_interval = [1,2]
        ans = [[1,2],[3,4],[5,6]]
        self.assertEqual(Solution().insert(intervals, new_interval), ans)
    def test_end(self):
        intervals = [[1,2], [3,4]]
        new_interval = [5,6]
        ans = [[1,2],[3,4],[5,6]]
        self.assertEqual(Solution().insert(intervals, new_interval), ans)
    def test_partial_overlap_end(self):
        intervals = [[1,2], [3,4]]
        new_interval = [4,6]
        ans = [[1,2],[3,6]]
        self.assertEqual(Solution().insert(intervals, new_interval), ans)
    def test_partial_overlap_beginning(self):
        intervals = [[1,2], [5,6]]
        new_interval = [3,5]
        ans = [[1,2],[3,6]]
        self.assertEqual(Solution().insert(intervals, new_interval), ans)
    def test_internal_overlap_intervals(self):
        intervals = [[1,2], [4,5], [7,8]]
        new_interval = [3,6]
        ans = [[1,2],[3,6], [7,8]]
        self.assertEqual(Solution().insert(intervals, new_interval), ans)
    def test_internal_overlap_new(self):
        intervals = [[1,2], [3,6], [7,8]]
        new_interval = [4,5]
        ans = [[1,2],[3,6], [7,8]]
        self.assertEqual(Solution().insert(intervals, new_interval), ans)
    def test_tripple_overlap(self):
        intervals = [[1,2], [3,6], [7,8]]
        new_interval = [2,7]
        ans = [[1,8]]
        self.assertEqual(Solution().insert(intervals, new_interval), ans)
    def test_empty_intervals(self):
        intervals = []
        new_interval = [1,8]
        ans = [[1,8]]
        self.assertEqual(Solution().insert(intervals, new_interval), ans)

unittest.main()
