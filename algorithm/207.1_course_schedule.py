# Course Schedule
# https://leetcode.com/problems/course-schedule/
# Completed 4/26/19

class Node:
    def __init__(self, label: int):
        self.label = label
        self.prerequisites = []
        self.children = []

    def add_prerequisite(self, node: 'Node') -> 'self':
        self.prerequisites.append(node)
        return self

    def add_child(self, node: 'Node') -> 'self':
        self.children.append(node)
        return self
        
    def is_leaf(self) -> bool:
        # Return True if node is a leaf
        return len(self.prerequisites) == 0

    def remove_leaf_from_children(self) -> 'self':
        # Remove pointers to this leaf that is stored on dependent nodes
        for child in self.children:
            child.prerequisites.remove(self)
        return self
        
class Tree:
    def __init__(self, node_count: int):
        self.nodes = [ Node(i) for i in range(node_count) ]

    def add_edges(self, edges: [[int, int]]) -> 'self':
        # List of integer pairs used to population node connections
        for edge in edges:
            current_class = self.nodes[edge[0]]
            prerequisit_class = self.nodes[edge[1]]
            current_class.add_prerequisite(prerequisit_class)
            prerequisit_class.add_child(current_class)
            
        return self

    def remove_leaf_from_tree(self, leaf: Node) -> 'self':
        self.nodes.remove(leaf)
        return self
            
    def prune_leaves(self) -> bool:
        # Remove all leaves and their references from tree.
        # Return True if leaves were removed and False otherwise.
        leaves = [ node for node in self.nodes if node.is_leaf() ]
        if len(leaves) == 0: return False
        
        for leaf in leaves:
            leaf.remove_leaf_from_children()
            self.remove_leaf_from_tree(leaf)
        return True

    def reduce_tree(self) -> [int]:
        # Return a list of cyclical nodes if they exist
        while self.prune_leaves(): pass
        return len(self.nodes) == 0

class Solution:
    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        return Tree(numCourses).add_edges(prerequisites).reduce_tree()

