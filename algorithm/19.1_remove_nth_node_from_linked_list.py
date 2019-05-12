# Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Completed 5/12/19

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        target = head
        last_node = head

        try:
            for _ in range(n + 1):
                last_node = last_node.next
        except:
            return head.next

        while last_node:
            target = target.next
            last_node = last_node.next

        target.next = target.next.next
        return head
        
#-------------------------------------------------------------------------------

