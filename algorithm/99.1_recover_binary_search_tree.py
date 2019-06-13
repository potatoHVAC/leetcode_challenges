#-------------------------------------------------------------------------------
#    Recover Binary Search Tree
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/recover-binary-search-tree/
# Completed 6/12/19
#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def recover_tree(root: TreeNode) -> None:
    """Fix binary search tree with two nodes swapped."""
    
    mem = {
        'previous': None,
        'first': None,
        'second': None
    }
    def _assign(node: TreeNode) -> None:
        """Update memory positions."""
        if mem['previous'] and node.val < mem['previous'].val:
            if not mem['first']:
                mem['first'] = mem['previous']
            mem['second'] = node
        mem['previous'] = node
    
    def _recover_tree(node: TreeNode):
        """In order traversal of bst."""
        if node:
            _recover_tree(node.left)
            _assign(node)
            _recover_tree(node.right)

    _recover_tree(root)
    mem['first'].val, mem['second'].val = mem['second'].val, mem['first'].val

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """Fix binary search tree with two nodes swapped.

        Input:
        :root: TreeNode -> root of broken bst
        """
        recover_tree(root)
