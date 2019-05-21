# Distribute Coins in Binary Tree
# https://leetcode.com/problems/distribute-coins-in-binary-tree/
# Completed 5/9/19
# Improved time with dynamic programming

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""Approach
1. Dynamic programming memoize setup
2. DFS
  2.1 Sum available coins and subtract (1 + any empty children) if available
  2.2 If no available coins, increase required coins counter
  2.3 Add all moved coins to total move
3. Pass up, (current available, current required, total moves)
"""

from helper_classes.binary_tree import *

class Solution:

    def __init__(self):
        self.memoize = {None: [0,0,0]}
        
    def distributeCoins(self, root: TreeNode) -> int:
        return self.dfs_distributeCoins(root)[2]
        
    def dfs_distributeCoins(self, root: TreeNode) -> [int]:
        """Find the distribution of coins for all nodes current and below

        Input:
        :root: TreeNode -- binary tree node to evaluate

        Output:
        [int] -- three integers as follows
          :output[0]: int -- all unallocated coins
          :output[1]: int -- all empty spaces
          :output[2]: int -- total moves made
        """
        if root not in self.memoize:
            available_left, required_left, moves_left = self.dfs_distributeCoins(root.left)
            available_right, required_right, moves_right = self.dfs_distributeCoins(root.right)
        
            available = root.val - 1 + available_left + available_right - required_left - required_right
            available = max(0, available)
            required = 1 - root.val + required_left + required_right - available_left - available_right
            required = max(0, required)
            total_moves = sum([
                available_left,
                available_right,
                required_left,
                required_right,
                moves_left,
                moves_right
            ])
            self.memoize[root] = [available, required, total_moves]
        return self.memoize[root]

#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):
    pass
