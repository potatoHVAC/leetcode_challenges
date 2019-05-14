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
        """Remove the node that is n places from the end of linked list.

        Input:
        :head: ListNode -- first node of the linked list
        :n:    int      -- target node index to be removed

        Output:
        ListNode -- head of the new linked list. None if list is now empty.
        """
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

