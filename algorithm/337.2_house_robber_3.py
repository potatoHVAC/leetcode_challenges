# House Robber III
# https://leetcode.com/problems/house-robber-iii/
# Completed 5/16/19

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""Approach
1. Use Dynamic programming 
2. If node's answer is already stored, return answer
3. Find value of robbing this house and skipping the next houses
4. Find value of skipping this house and maybe robbing the next houses
5. Store seteps 3 and 4 for that node.
"""

from helper_classes.bst import *

class Solution:

    def __init__(self):
        self.memoize = {None: [0,0]}
        
    def rob(self, root: TreeNode) -> int:
        """Return the maximum possible haul from this job.

        Input:
        :root:   TreeNode -- root node of the house tree
        :danger: bool     -- True if the previous house was burgled

        Output:
        int -- highest possible haul from the neighborhood
        """
        def _rob(root: TreeNode) -> [[int]]:
            if root not in self.memoize:
                left_rob, left_skip = _rob(root.left)
                right_rob, right_skip = _rob(root.right)

                rob_current = root.val + left_skip + right_skip
                skip_current = max(left_rob, left_skip) + max(right_rob, right_skip)
                self.memoize[root] = [rob_current, skip_current]
            return self.memoize[root]
        
        return max(_rob(root))

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
    
