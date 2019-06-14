#-------------------------------------------------------------------------------
#    Merge Two Sorted Lists
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/merge-two-sorted-lists/
# Completed 6/13/19
#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def merge(list1: ListNode, list2: ListNode) -> ListNode:
    """Merge two sorted linked lists and return head of new list."""
    new_head = new_node = ListNode(None)

    def _merge(list1: ListNode, list2: ListNode, new_node: ListNode) -> None:
        if not list1:
            new_node.next = list2
            return
        if not list2:
            new_node.next = list1
            return

        if list1.val < list2.val:
            new_node.next = list1
            _merge(list1.next, list2, new_node.next)
        else:
            new_node.next = list2
            _merge(list1, list2.next, new_node.next)

    _merge(list1, list2, new_node)
    return new_head.next

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Merge two sorted linked lists and return head of new list.

        Input:
        :l1: ListNode -> head of first sorted linked list
        :l2: ListNode -> head of second sorted linked list

        Output:
        ListNode -> head of merged linked list
        """
        return merge(l1, l2)
