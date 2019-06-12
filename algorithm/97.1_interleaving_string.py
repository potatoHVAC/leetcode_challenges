#-------------------------------------------------------------------------------
#    Interleaving String
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/interleaving-string/
# Completed 6/12/19
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Use two pointers and Dynamic.
2. Check if pointers have been solved already.
3. If one of the strings is empty check if the remaining string matches what is
    left of the input.
4. If either of the strings current pointers match the target's next letter
    then check those paths accordingly.
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def is_interleave(string1: str, string2: str, string3: str) -> bool:
    """Return True if :string1: is interleaved by :string1: and :string2:"""
    if len(string1) + len(string2) != len(string3):
        return False

    memoize = {}
    def _is_interleave(spt1: int, spt2: int) -> bool:
        if (spt1, spt2) not in memoize:
            ans = False
            
            if spt1 == len(string1) or spt2 == len(string2):
                ans = (string1[spt1:] + string2[spt2:] == string3[spt1+spt2:])

            else:
                if string1[spt1] == string3[spt1+spt2]:
                    ans |= _is_interleave(spt1+1, spt2)
                if string2[spt2] == string3[spt1+spt2]:
                    ans |= _is_interleave(spt1, spt2+1)
                
            memoize[(spt1, spt2)] = ans
            
        return memoize[(spt1, spt2)]

    return _is_interleave(0,0)

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """Return True if :s3: is interleaved by :s1: and :s2:

        Input:
        :s1: str 
        :s2: str
        :s3: str -> target

        Output:
        bool -> True if :s3: is interleaved by :s1: and :s2:
        """
        return is_interleave(s1, s2, s3)

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_simple(self):
        string1 = 'a'
        string2 = 'b'
        string3 = 'ab'
        self.assertTrue(Solution().isInterleave(string1, string2, string3))
    def test_repeat(self):
        string1 = 'aa'
        string2 = 'bb'
        string3 = 'abab'
        self.assertTrue(Solution().isInterleave(string1, string2, string3))
    def test_concatenated(self):
        string1 = 'aa'
        string2 = 'bb'
        string3 = 'aabb'
        self.assertTrue(Solution().isInterleave(string1, string2, string3))
    def test_empty(self):
        string1 = ''
        string2 = 'bb'
        string3 = 'bb'
        self.assertTrue(Solution().isInterleave(string1, string2, string3))

    def test_overlap(self):
        string1 = 'aa'
        string2 = 'aa'
        string3 = 'aa'
        self.assertFalse(Solution().isInterleave(string1, string2, string3))
    def test_out_of_order(self):
        string1 = 'aaa'
        string2 = 'abc'
        string3 = 'aacaab'
        self.assertFalse(Solution().isInterleave(string1, string2, string3))
        
unittest.main()
