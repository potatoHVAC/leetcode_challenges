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
        smaller_root = smaller_head = ListNode(None)
        larger_root = larger_head = ListNode(None)

        while head:
            if head.val < target:
                smaller_head.next = head
                smaller_head = head
            else:
                larger_head.next = head
                larger_head = head
            head = head.next
        larger_head.next = None
        smaller_head.next = larger_root.next
        return smaller_root.next

