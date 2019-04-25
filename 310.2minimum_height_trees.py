# Minimum height Tree
# https://leetcode.com/problems/minimum-height-trees/submissions/
# Completed 4/24/19

class Node:
    def __init__(self, label):
        self.label = label
        self.connections = []

    def add_connection(self, node):
        self.connections.append(node)

    def is_leaf(self):
        return len(self.connections) == 1

    def remove_leaf_from_connection(self):
        self.connections[0].connections.remove(self)
        
class Tree:
    def __init__(self, n):
        self.nodes = [ Node(i) for i in range(n) ]

    def add_edges(self, edges):
        for edge in edges:
            start_node = self.nodes[edge[0]]
            end_node = self.nodes[edge[1]]

            start_node.add_connection(end_node)
            end_node.add_connection(start_node)

    def remove_leaf_from_tree(self, node):
        self.nodes.remove(node)
            
    def prune_leaves(self):
        leaves = [ node for node in self.nodes if node.is_leaf() ]
        for leaf in leaves:
            leaf.remove_leaf_from_connection()
            self.remove_leaf_from_tree(leaf)

    def solve_mht(self):
        while len(self.nodes) > 2:
            self.prune_leaves()

        return [ node.label for node in self.nodes ]

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = Tree(n)
        tree.add_edges(edges)
        return tree.solve_mht()

