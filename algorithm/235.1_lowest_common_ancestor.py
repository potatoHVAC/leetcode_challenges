# Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Completed 5/2/19

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
