# Vertical Order Traversal of a Binary Tree
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# Completed 5/6/19

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
    
class Solution:
    
    def verticalTraversal(self, root: TreeNode) -> [[int]]:
        self.tree_count = {}
        return self.traverse_tree(root).show_tree_count()

    def flatten_arr(self, array_2d: [list]) -> list:
        # Return a flattened array
        return [ val for sub_list in array_2d for val in sub_list ]
    
    def flatten_dict(self, dictionary) -> ['elements']:        
        # Return list of dictionary elements ordered by key
        keys = list(dictionary)
        keys.sort()
        return [ dictionary[key] for key in keys ]

    def show_tree_count(self) -> [[int]]:
        # Return list of lists representing node values ordered by verticals
        output = []
        for vertical in self.flatten_dict(self.tree_count):
            output.append(self.flatten_arr(self.flatten_dict(vertical)))
        return output
    
    def add_count(self, node: TreeNode, pos: int, depth: int) -> 'self':
        # Add node to self.tree_count
        if node.val is not None:
            if pos not in self.tree_count: self.tree_count[pos] = {}
            self.add_val_to_depth(node, pos, depth)
        return self
                
    def add_val_to_depth(self, node: TreeNode, pos: int, depth: int):
        # Add node to the correct depth in self.tree_count
        if depth not in self.tree_count[pos]: self.tree_count[pos][depth] = []
        self.tree_count[pos][depth].append(node.val)
        self.tree_count[pos][depth].sort()
            
    def traverse_tree(self, root, pos: int = 0, depth: int = 0) -> 'self':
        # Traverse BST and insert node into self.tree_count
        if root:
            self.add_count(root, pos, depth)
            if root.left: self.traverse_tree(root.left, pos - 1, depth + 1)
            if root.right: self.traverse_tree(root.right, pos + 1, depth + 1)
        return self
