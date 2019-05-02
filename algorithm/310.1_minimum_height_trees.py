# Minimum height Tree
# https://leetcode.com/problems/minimum-height-trees/submissions/
# Completed 4/24/19

class Node:
    def __init__(self, label: int):
        self.label = label
        self.connections = []

    def add_connection(self, node: 'Node') -> 'self':
        self.connections.append(node)
        return self

    def is_leaf(self) -> bool:
        # Return True if node is a leaf
        return len(self.connections) == 1

    def remove_leaf_from_connection(self) -> 'self':
        # Remove pointers to this leaf that is stored on other node
        self.connections[0].connections.remove(self)
        return self
        
class Tree:
    def __init__(self, node_count: int):
        self.nodes = [ Node(i) for i in range(node_count) ]

    def add_edges(self, edges: [[int, int]]) -> 'self':
        # List of integer pairs used to population node connections
        for edge in edges:
            start_node = self.nodes[edge[0]]
            end_node = self.nodes[edge[1]]
            start_node.add_connection(end_node)
            end_node.add_connection(start_node)

        return self

    def remove_leaf_from_tree(self, leaf: Node) -> self:
        self.nodes.remove(leaf)
        return self
            
    def prune_leaves(self) -> 'self':
        # Remove any node that is a leaf of the tree and removes their reference from connected node
        leaves = [ node for node in self.nodes if node.is_leaf() ]
        for leaf in leaves:
            leaf.remove_leaf_from_connection()
            self.remove_leaf_from_tree(leaf)
        reeturn self

    def reduce_tree(self) -> [int]:
        # Return a list of the last one or two node labels that would be the roots of a minimum height tree
        while len(self.nodes) > 2: self.prune_leaves()
        return [ node.label for node in self.nodes ]

class Solution:
    def findMinHeightTrees(self, node_count: int, edges: [[int]]) -> [int]:
        return Tree(node_count).add_edges(edges).reduce_tree()

