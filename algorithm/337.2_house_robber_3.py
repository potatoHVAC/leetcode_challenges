# House Robber III
# https://leetcode.com/problems/house-robber-iii/
# Completed 5/16/19

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
