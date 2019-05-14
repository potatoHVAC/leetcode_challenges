# Course Schedule
# https://leetcode.com/problems/course-schedule/
# Completed 4/26/19

''' Approach
1. Create a doubly linked graph.
2. Remove leaf nodes from tree and delete their references in parent nodes.
3. Repeat 2 untill tree is empty or no more leaves exist.
4. Return True if tree is empty.
'''

class Node:
    def __init__(self, label: int):
        self.label = label
        self.prerequisites = []
        self.children = []

    def add_prerequisite(self, node: 'Node') -> 'self':
        """Add prerequisite to node."""
        self.prerequisites.append(node)
        return self

    def add_child(self, node: 'Node') -> 'self':
        """Add child to node."""
        self.children.append(node)
        return self
        
    def is_leaf(self) -> bool:
        """Return True if node is a leaf."""
        return len(self.prerequisites) == 0

    def remove_leaf_from_children(self) -> 'self':
        """Remove node references from all parent nodes."""
        for child in self.children:
            child.prerequisites.remove(self)
        return self
        
class Tree:
    def __init__(self, node_count: int):
        self.nodes = [ Node(i) for i in range(node_count) ]

    def add_edges(self, edges: [[int, int]]) -> 'self':
        """Add all node relationships defined in edges.
        
        Input:
        :edges: [[int, int]] -- list containint sets of integers that represent
            relationships between nodes
        """
        for edge in edges:
            current_class = self.nodes[edge[0]]
            prerequisit_class = self.nodes[edge[1]]
            current_class.add_prerequisite(prerequisit_class)
            prerequisit_class.add_child(current_class)
            
        return self

    def remove_leaf_from_tree(self, leaf: Node) -> 'self':
        """Remove leaf from tree."""
        self.nodes.remove(leaf)
        return self
            
    def prune_leaves(self) -> bool:
        """Find all leaves and remove them from tree.

        Output:
        True  -- if leaves are removed
        False -- if no leaves in tree
        """
        leaves = [ node for node in self.nodes if node.is_leaf() ]
        if len(leaves) == 0: return False
        
        for leaf in leaves:
            leaf.remove_leaf_from_children()
            self.remove_leaf_from_tree(leaf)
        return True

    def reduce_tree(self) -> [int]:
        """Remove leaves from tree until tree is empty or no more leaves exist.

        Output:
        True  -- if tree is empty
        False -- if tree contains cycles
        """
        while self.prune_leaves(): pass
        return len(self.nodes) == 0

class Solution:
    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        return Tree(numCourses).add_edges(prerequisites).reduce_tree()

#-------------------------------------------------------------------------------

import unittest

class TestSolution(unittest.TestCase):

    def test_canFinish_2_pass(self):
        tree = Tree(2).add_edges([[0,1]])
        self.assertTrue(tree.reduce_tree())
    def test_canFinish_4_pass(self):
        tree = Tree(4).add_edges([[0,1], [0,2], [0,3]])
        self.assertTrue(tree.reduce_tree())
    def test_canFinish_2_fail(self):
        tree = Tree(2).add_edges([[0,1],[1,0]])
        self.assertFalse(tree.reduce_tree())
        
unittest.main()
