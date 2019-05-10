# House Robber III
# https://leetcode.com/problems/house-robber-iii/
# Completed 5/16/19

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from tree_class import *

class Solution:

    def __init__(self):
        self.memoize = {None: [0,0]}
        
    def rob(self, root: TreeNode) -> int:
        def _rob(root: TreeNode) -> [[int]]:
            if root not in self.memoize:
                left_rob, left_skip = _rob(root.left)
                right_rob, right_skip = _rob(root.right)
                self.memoize[root] = [
                    root.val + left_skip + right_skip,
                    max([left_rob, left_skip]) + max([right_rob, right_skip])
                ]
            return self.memoize[root]
        
        return max(_rob(root))

#-------------------------------------------------------------------------------
    
import unittest

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
    
