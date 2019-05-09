# Distribute Coins in Binary Tree
# https://leetcode.com/problems/distribute-coins-in-binary-tree/
# Completed 5/9/19
# Improved time with dynamic programming

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        self.memoize = {None: [0,0,0]}
        
    def distributeCoins(self, root: TreeNode) -> int:
        return self.dfs_distributeCoins(root)[2]
        
    def dfs_distributeCoins(self, root: TreeNode) -> [int]:
        # Return the counts for the available coins, sitll required coins, and total moves at current node.
        if root not in self.memoize:
            available_left, required_left, moves_left = self.dfs_distributeCoins(root.left)
            available_right, required_right, moves_right = self.dfs_distributeCoins(root.right)
        
            available = root.val - 1 + available_left + available_right - required_left - required_right
            available = max(0, available)
            required = 1 - root.val + required_left + required_right - available_left - available_right
            required = max(0, required)
            total_moves = sum([
                available_left,
                available_right,
                required_left,
                required_right,
                moves_left,
                moves_right
            ])
            self.memoize[root] = [available, required, total_moves]
        return self.memoize[root]
