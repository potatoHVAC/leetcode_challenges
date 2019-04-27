# Course Schedule
# https://leetcode.com/problems/course-schedule/
# Completed 4/26/19

class Node:
    def __init__(self, label):
        self.label = label
        self.prerequisites = []
        self.children = []

    def add_prerequisite(self, node):
        self.prerequisites.append(node)

    def add_child(self, node):
        self.children.append(node)
        
    def is_leaf(self):
        '''
        output: bool -> True if node is a leaf
        '''
        return len(self.prerequisites) == 0

    def remove_leaf_from_children(self):
        # Removes pointers to this leaf that is stored on nodes that require this class
        for child in self.children:
            child.prerequisites.remove(self)
        
class Tree:
    def __init__(self, n):
        self.nodes = [ Node(i) for i in range(n) ]

    def add_edges(self, edges):
        '''
        input: list of [int, int] -- List of connections used for populating node relationships
        '''
        for edge in edges:
            current_class = self.nodes[edge[0]]
            prerequisit_class = self.nodes[edge[1]]
            current_class.add_prerequisite(prerequisit_class)
            prerequisit_class.add_child(current_class)

    def remove_leaf_from_tree(self, leaf):
        self.nodes.remove(leaf)
            
    def prune_leaves(self):
        '''
        output: bool -> False if tree has no leaves

        Removes any node that is a leaf of the tree and removes their reference from connected node
        '''
        leaves = [ node for node in self.nodes if node.is_leaf() ]
        if len(leaves) == 0: return False
        
        for leaf in leaves:
            leaf.remove_leaf_from_children()
            self.remove_leaf_from_tree(leaf)
        return True

    def solve_mht(self):
        '''
        output: list of ints -- list of labels that indicate nodes for the minimum height trees
        '''
        while self.prune_leaves(): pass
        return len(self.nodes) == 0

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        schedule = Tree(numCourses)
        schedule.add_edges(prerequisites)
        return schedule.solve_mht()
