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

"""Approach
1. Use recursion 
2. If danger (prevous house was robbed)
  2.1 return the value of not robbing this house and maybe robbing the next
3. If not in danger (prevous house was not robbed)
  3.1 find value of robbing this house and maybe robbing the next
  3.2 find value of not robbing this house and maybe robbing the next
  3.3 return the max of 3.1 and 3.2
"""

from helper_classes.bst import *

class Solution:
    
    def rob(self, root: TreeNode, danger: bool = False) -> int:
        """Return the maximum possible haul from this job.

        Input:
        :root:   TreeNode -- root node of the house tree
        :danger: bool     -- True if the previous house was burgled

        Output:
        int -- highest possible haul from the neighborhood
        """
        if not root:
            return 0
        
        if danger:
            return self.rob(root.left) + self.rob(root.right)
        else:
            rob_current = root.val + self.rob(root.left, True) + self.rob(root.right, True)
            skip_current = self.rob(root.left) + self.rob(root.right)
            return max(rob_current, skip_current)

#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_rob_2_nodes_rob_root(self):
        tree = BST().insert_array([5, 1])
        self.assertEqual(Solution().rob(tree.root), 5)
    def test_rob_2_nodes_rob_leaf(self):
        tree = BST().insert_array([1, 5])
        self.assertEqual(Solution().rob(tree.root), 5)
    def test_rob_4_nodes_skip_two(self):
        tree = BST().insert_array([5, 1, 2, 4])
        self.assertEqual(Solution().rob(tree.root), 9)
    def test_rob_5_node_skip_three(self):
        tree = BST().insert_array([1, 10, 2, 3, 9])
        self.assertEqual(Solution().rob(tree.root), 19)
    def test_rob_11_nodes(self):
        tree = BST().insert_array([4, 2, 10, 1, 3, 5, 12, 6, 11, 13, 9])
        self.assertEqual(Solution().rob(tree.root), 47)
        
unittest.main()
