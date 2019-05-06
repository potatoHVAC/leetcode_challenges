# Smallest String Starting From Leaf
# https://leetcode.com/problems/smallest-string-starting-from-leaf/
# Completed 5/6/19

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def to_letter(node: TreeNode) -> str:
    letters = "abcdefghijklmnopqrstuvwxyz"
    return letters[node.val]

class Solution:
    def smallestFromLeaf(self, root: TreeNode, path: str = "") -> str:
        if root is None: return path
        
        path = to_letter(root) + path
        if root.left and root.right:
            return min([self.smallestFromLeaf(root.left, path), self.smallestFromLeaf(root.right, path)])
        elif root.left:
            return self.smallestFromLeaf(root.left, path)
        else:
            return self.smallestFromLeaf(root.right, path)
