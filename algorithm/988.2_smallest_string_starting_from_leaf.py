# Smallest String Starting From Leaf
# https://leetcode.com/problems/smallest-string-starting-from-leaf/
# Completed 5/6/19
# I added dynamic 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def to_letter(node: TreeNode) -> str:
    # Return the letter equivalent of node.val
    letters = "abcdefghijklmnopqrstuvwxyz"
    return letters[node.val]

class Solution:

    def __init__(self):
        self.memoize = {}

    def smallestFromLeaf(self, root: TreeNode) -> str:
        def _smallestFromLeaf(root: TreeNode, path: str) -> str:
            if root is None: return path
            
            if root not in self.memoize:
                path = to_letter(root.val) + path
                
                if root.left and root.right:
                    left = _smallestFromLeaf(root.left, path)
                    right = _smallestFromLeaf(root.right, path)
                    self.memoize[root] = min(left, right)
                elif root.left:
                    self.memoize[root] = _smallestFromLeaf(root.left, path)
                else:
                    self.memoize[root] = _smallestFromLeaf(root.right, path)
                    
            return self.memoize[root]
        return _smallestFromLeaf(root, "")
