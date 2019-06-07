#-------------------------------------------------------------------------------
#    Jump Game II
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/jump-game-ii/
# Almost Completed 6/6/19
# TO for large inputs
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Dynamic Solution
2. Create platform object with jump size and number of jumps to end (initialized
    as None).
3. Set last platform to_end = 0.
4. Each platform looks at all forward positions and returns the smallest to_end
    setting it's own to_end to the smallest + 1.
5. Return the first platforms to_end.
"""

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

class Platform:

    def __init__(self, size):
        self.size = size
        self.to_end = None

class Jump:

    def __init__(self, nums: [int]):
        self.pads = [ Platform(n) for n in nums ]
        self.pads[-1].to_end = 0

    def solve(self):
        """Return the smallest number of jumps to last position"""
        
        def _solve(pointer: int) -> int:
            if pointer >= len(self.pads):
                return 0

            platform = self.pads[pointer]
            if self.pads[pointer].to_end is None:
                jump_size = platform.size
                if jump_size == 0:
                    platform.to_end = float('inf')
                else:
                    shortest = min([
                        _solve(pointer + n) for n in range(1, jump_size + 1)
                    ])
                    platform.to_end = shortest + 1

            return platform.to_end

        return _solve(0)

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def jump(self, nums: [int]) -> int:
        return Jump(nums).solve()

#-------------------------------------------------------------------------------
#    Unit Test
#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_1(self):
        nums = [1]
        ans = 0
        self.assertEqual(Solution().jump(nums), ans)
    def test_1s(self):
        nums = [1,1,1,1,1,1,1,1,1,1]
        ans = 9
        self.assertEqual(Solution().jump(nums), ans)
    def test_ex1(self):
        nums = [2,3,1,1,4]
        ans = 2
        self.assertEqual(Solution().jump(nums), ans)
    def test_overshoot(self):
        nums = [5,1]
        ans = 1
        self.assertEqual(Solution().jump(nums), ans)
    def test_zeros(self):
        nums = [5,0,0,0,0,1]
        ans = 1
        self.assertEqual(Solution().jump(nums), ans)

unittest.main()
