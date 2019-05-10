# Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Completed 5/2/19

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

''' Approach
1 Create find_path that traverses the tree and finds path to a given node.
2 Find the path to higher and lower bounds. 
3 Iterate through path index and return the last node with matching value.
'''

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', low: 'TreeNode', high: 'TreeNode') -> 'TreeNode':
        lower_path = self.find_path(root, low)
        higher_path = self.find_path(root, high)
        return self.compare_paths(lower_path, higher_path)

    def find_path(self, root: 'TreeNode', target: 'TreeNode') -> ['TreeNode']:
        # Recursively find the path to target node
        def _find_path(root: 'TreeNode', target: 'TreeNode', path: ['TreeNode']) -> ['TreeNode']:
            path.append(root)
            if root == target:
                return path

            if root.val > target.val:
                return _find_path(root.left, target, path)
            else:
                return _find_path(root.right, target, path)
            
        return _find_path(root, target, [])

    def compare_paths(self, lower_path: ['TreeNode'], higher_path: ['TreeNode']) -> 'TreeNode':
        # Find the largest index where 'lower_path[index] == higher_path[index]'
        for i, node in enumerate(lower_path):
            # If the ith nodes dont match, return the previous node
            if node != higher_path[i]: return higher_path[i - 1]
            # If higher_path is out of nodes, return its last node
            if i + 1 == len(higher_path): return node
        # If lower_path is out of nodes, return its last node
        return lower_path[-1]

#-------------------------------------------------------------------------------

import unittest
from tree_class import *

class TestSolution(unittest.TestCase):

    def test_2_node_tree(self):
        tree = Tree().insert_array([1, 2])
        self.assertEqual(Solution().lowestCommonAncestor(
            tree.root,
            tree.find_node(1),
            tree.find_node(2)
        ).val, 1)
    def test_3_node_tree(self):
        tree = Tree().insert_array([2, 1, 3])
        self.assertEqual(Solution().lowestCommonAncestor(
            tree.root,
            tree.find_node(1),
            tree.find_node(3)
        ).val, 2)
    def test_9_node_tree(self):
        tree = Tree().insert_array([6,2,8,0,4,7,9,None,None,3,5])
        self.assertEqual(Solution().lowestCommonAncestor(
            tree.root,
            tree.find_node(2),
            tree.find_node(8)
        ).val, 6)
    def test_9_node_tree_with_lower_input_as_ancestor(self):
        tree = Tree().insert_array([6,2,8,0,4,7,9,None,None,3,5])
        self.assertEqual(Solution().lowestCommonAncestor(
            tree.root,
            tree.find_node(2),
            tree.find_node(4)
        ).val, 2)

unittest.main()
