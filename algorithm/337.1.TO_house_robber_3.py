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
    
    def rob(self, root: TreeNode, danger: bool = False) -> int:
        if not root:
            return 0
        
        if danger:
            return self.rob(root.left) + self.rob(root.right)
        else:
            return max([
                root.val + self.rob(root.left, True) + self.rob(root.right, True),
                self.rob(root.left) + self.rob(root.right)
            ])
