# Swap Nodes In Pairs
# https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1681/
# Completed 5/5/19

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head: return head
        new_head = head.next
        if new_head:
            new_head.next, head.next  = head, self.swapPairs(new_head.next)
            return new_head
        else:
            return head
