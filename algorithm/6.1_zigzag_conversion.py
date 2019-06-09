#-------------------------------------------------------------------------------
#    ZigZag Conversion
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/zigzag-conversion/
# Completed 6/8/19
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Crete zigzag object with lists for each row.
2. Insert each string element into lists from top to bottom.
3. Join all rows together and return string.
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

class ZigZag:

    def __init__(self, string: str, row_count: int):
        self.input_str = string
        self.row_count = row_count
        self.zigzag = [ [] for _ in range(row_count) ]
        self._zag_that_zig()

    def _zag_that_zig(self) -> 'self':
        """Populate :self.zigzag: based on number of rows."""

        def _insert(pointer: int, row_pointer: int, step: int):
            if pointer == len(self.input_str):
                return
            elif row_pointer == -1:
                _insert(pointer, 1, 1)
            elif row_pointer == self.row_count:
                _insert(pointer, max(0, self.row_count - 2), -1)
            else:
                self.zigzag[row_pointer].append(self.input_str[pointer])
                _insert(pointer + 1, row_pointer + step, step)

        _insert(0, 0, 1)
        return self

    def to_s(self) -> str:
        """Return :self.zigzag: formatted as string."""
        return "".join([ "".join(row) for row in self.zigzag ])

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """Return s formatted as zigzag based on number of rows.

        Input:
        :s:       str -> input string
        :numRows: int -> number of rows for ZigZag

        Output:
        str -> ZigZag formatted into string
        """
        return ZigZag(s, numRows).to_s()

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_a_1(self):
        string = 'a'
        row_count = 1
        ans = 'a'
        self.assertEqual(Solution().convert(string, row_count), ans)
    def test_a_2(self):
        string = 'a'
        row_count = 2
        ans = 'a'
        self.assertEqual(Solution().convert(string, row_count), ans)
    def test_abc_1(self):
        string = 'abc'
        row_count = 1
        ans = 'abc'
        self.assertEqual(Solution().convert(string, row_count), ans)
    def test_abcde_2(self):
        string = 'abcde'
        row_count = 2
        ans = 'acebd'
        self.assertEqual(Solution().convert(string, row_count), ans)
    def test_ex1(self):
        string = 'PAYPALISHIRING'
        row_count = 3
        ans = 'PAHNAPLSIIGYIR'
        self.assertEqual(Solution().convert(string, row_count), ans)
    def test_ex2(self):
        string = 'PAYPALISHIRING'
        row_count = 4
        ans = 'PINALSIGYAHRPI'
        self.assertEqual(Solution().convert(string, row_count), ans)

unittest.main()
