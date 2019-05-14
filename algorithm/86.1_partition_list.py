# Partition List
# https://leetcode.com/problems/partition-list/
# Completed 5/8/19

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""Approach
1. Create dummy linked lists to hold the lower values and the >= values
2. Create pointers for roots and heads of each list.
3. Itterate through input list and add each node to the heads of their 
   target lists based on less than and >=.
4. Add the >= list to the end of the smaller list (removing the dummy root).
5. Return the root.next of the smaller list. 
"""

class Solution:
    def partition(self, head: ListNode, target: int, ) -> ListNode:
        """Return the head of a partitioned linked list.

        Input:
        :head:   ListNode -- head of unpartitioned linked list
        :target: int      -- value to partition list around

        Output:
        ListNode -- root node of partitioned linked list
        """
        smaller_root = ListNode(-2)
        larger_root = ListNode(-1)
        smaller_head = self.segregate(head, smaller_root, larger_root, target)
        smaller_head.next = larger_root.next
        return smaller_root.next

    def insert(self, head: ListNode, child_node: ListNode) -> ListNode:
        """Add new node to the head of list"""
        head.next = child_node
        return child_node

    def segregate(self,
                  head: ListNode,
                  smaller_head: ListNode,
                  larger_head: ListNode,
                  target: int
    ) -> ListNode:
        """Seperate linked liste based on target value

        Input:
        :head:         ListNode -- head node to partition
        :smaller_head: ListNode -- head of smaller values list
        :larger_head:  ListNode -- head of equal and larger values list
        :target:       int      -- target value to partition around

        Output:
        ListNode -- head of the smaller values list
        """
        if head is None:
            smaller_head.next = None
            larger_head.next = None
            return smaller_head

        if head.val < target: smaller_head = self.insert(smaller_head, head)
        else: larger_head = self.insert(larger_head, head)
        return self.segregate(head.next, smaller_head, larger_head, target)

