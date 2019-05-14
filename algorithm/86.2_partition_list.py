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
        :head:   ListNode -- head of input list
        :target: int      -- target value to partition around

        Output:
        ListNode -- head of partitioned linked list
        """
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

