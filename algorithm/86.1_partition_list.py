# Partition List
# https://leetcode.com/problems/partition-list/
# Completed 5/8/19

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, target: int, ) -> ListNode:
        smaller_root = ListNode(-2)
        larger_root = ListNode(-1)
        smaller_head = self.segregate(head, smaller_root, larger_root, target)
        smaller_head.next = larger_root.next
        return smaller_root.next

    def insert(self, parent_node: ListNode, child_node: ListNode) -> ListNode:
        parent_node.next = child_node
        return child_node

    def segregate(self, head: ListNode, smaller_head: ListNode, larger_head: ListNode, target: int) -> ListNode:
        if head is None:
            smaller_head.next = None
            larger_head.next = None
            return smaller_head

        if head.val < target: smaller_head = self.insert(smaller_head, head)
        else: larger_head = self.insert(larger_head, head)
        return self.segregate(head.next, smaller_head, larger_head, target)

