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
        """Return True if node is a leaf."""
        return len(self.connections) == 1

    def remove_leaf_from_connection(self) -> 'self':
        """Remove all references to this node on connected nodes."""
        self.connections[0].connections.remove(self)
        return self
        
class Tree:
    def __init__(self, node_count: int):
        self.nodes = [ Node(i) for i in range(node_count) ]

    def add_edges(self, edges: [[int, int]]) -> 'self':
        """Add connections to nodes based on input edges.
        
        Input:
        :edges: [[int]] -- list of sets of integers that define two nodes relationship
        """
        for edge in edges:
            start_node = self.nodes[edge[0]]
            end_node = self.nodes[edge[1]]
            start_node.add_connection(end_node)
            end_node.add_connection(start_node)

        return self

    def remove_leaf_from_tree(self, leaf: Node) -> 'self':
        """Remove node from tree."""
        self.nodes.remove(leaf)
        return self
            
    def prune_leaves(self) -> 'self':
        """Locate all current leaves and remove them from tree exposing new leaves."""
        leaves = [ node for node in self.nodes if node.is_leaf() ]
        for leaf in leaves:
            leaf.remove_leaf_from_connection()
            self.remove_leaf_from_tree(leaf)
        return self

    def reduce_tree(self) -> [int]:
        """Remove leaves from tree exposing new leaves unitl only one or two nodes remain.
        input tree must be binary otherwise function will hang.

        Output:
        [int] -- list of node values
        """
        while len(self.nodes) > 2: self.prune_leaves()
        return sorted([ node.label for node in self.nodes ])

class Solution:
    def findMinHeightTrees(self, node_count: int, edges: [[int]]) -> [int]:
        """Return nodes that would be used to make this tree have its minimum height.

        Input:
        :node_count: int     -- number of nodes in tree
        :edges:      [[int]] -- list of sets of integers that define two nodes relationship
        
        Output:
        [int] -- list of node values
        """
        return Tree(node_count).add_edges(edges).reduce_tree()

#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_findMinheightTrees_4_nodes(self):
        n = 4
        edges = [[1, 0], [1, 2], [1, 3]]
        self.assertEqual(Solution().findMinHeightTrees(n, edges), [1])
    def test_findMinheightTrees_1_node(self):
        n = 1
        edges = []
        self.assertEqual(Solution().findMinHeightTrees(n, edges), [0])
    def test_findMinheightTrees_2_nodes(self):
        n = 2
        edges = [[1, 0]]
        self.assertEqual(Solution().findMinHeightTrees(n, edges), [0, 1])
    def test_findMinheightTrees_6_nodes(self):
        n = 6
        edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
        self.assertEqual(Solution().findMinHeightTrees(n, edges), [3, 4])

unittest.main()
