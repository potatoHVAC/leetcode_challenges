# Binary Tree Class for unit testing

from helper_classes.tree_node import *

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, node: TreeNode, values: [int], value_pointer: int) -> [TreeNode]:
        # Insert values into children
        if node is None: return [None, None]
        
        if values[value_pointer]:
            node.left = TreeNode(values[value_pointer])
        if value_pointer + 1 < len(values) and values[value_pointer + 1]:
            node.right = TreeNode(values[value_pointer + 1])
        return [node.left, node.right]

    def build_tree(self, values: [int]) -> 'self':
        # Build tree from list
        self.root = TreeNode(values[0])
        node_queue = [self.root]
        value_pointer = 1
        while value_pointer < len(values):
            node_queue += self.insert(node_queue.pop(0), values, value_pointer)
            value_pointer += 2
        return self

