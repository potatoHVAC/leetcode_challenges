# Minimum Height Tree
# https://leetcode.com/problems/minimum-height-trees/submissions/
# Almost completed on 4/24
# This is a solution but it is brute force and times out for larger inputs.

class Node:
    def __init__(self, label):
        self.label = label
        self.connections = []

    def add_connection(self, node):
        self.connections.append(node)

    def check_height(self, previous_node = False):
        # Recursively find tree height by breadth first search 
        if previous_node and len(self.connections) <= 1:
            return 0
        else:
            return max([ 1 + node.check_height(self) for node in self.connections if node != previous_node ])
        
class Tree:
    def __init__(self, n):
        self.nodes = [ Node(i) for i in range(n) ]

    def add_edges(self, edges):
        '''
        input: list of [int, int] -- List of connections used for populating node relationships
        '''
        for edge in edges:
            start_node = self.nodes[edge[0]]
            end_node = self.nodes[edge[1]]

            start_node.add_connection(end_node)
            end_node.add_connection(start_node)

    def solve_mht(self):
        '''
        output: list of ints -- list of labels that indicate nodes for the minimum height trees
        '''
        if len(self.nodes) == 1:
            return [0]
        else:
            node_heights = [ node.check_height() for node in self.nodes ]
            min_height = min(node_heights)
            return [ i for i, height in enumerate(node_heights) if height == min_height ]

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = Tree(n)
        tree.add_edges(edges)
        return tree.solve_mht()
