# House Robber III
# https://leetcode.com/problems/house-robber-iii/
# Almost Completed 5/6/19
# Brute force recursion fails on large inputs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def rob(self, root: 'TreeNode', danger: bool = False) -> int:
        if not root:
            return 0
        
        if danger:
            return self.rob(root.left) + self.rob(root.right)
        else:
            return max([
                root.val + self.rob(root.left, True) + self.rob(root.right, True),
                self.rob(root.left) + self.rob(root.right)
            ])

#-------------------------------------------------------------------------------

import unittest
from tree_class import *

class TestSolution(unittest.TestCase):

    def test_rob_2_nodes_rob_root(self):
        tree = Tree().insert_array([5, 1])
        self.assertEqual(Solution().rob(tree.root), 5)
    def test_rob_2_nodes_rob_leaf(self):
        tree = Tree().insert_array([1, 5])
        self.assertEqual(Solution().rob(tree.root), 5)
    def test_rob_4_nodes_skip_two(self):
        tree = Tree().insert_array([5, 1, 2, 4])
        self.assertEqual(Solution().rob(tree.root), 9)
    def test_rob_5_node_skip_three(self):
        tree = Tree().insert_array([1, 10, 2, 3, 9])
        self.assertEqual(Solution().rob(tree.root), 19)
    def test_rob_11_nodes(self):
        tree = Tree().insert_array([4, 2, 10, 1, 3, 5, 12, 6, 11, 13, 9])
        self.assertEqual(Solution().rob(tree.root), 47)
        
unittest.main()
