#-------------------------------------------------------------------------------
#    Reverse Nodes in k-Groups
#-------------------------------------------------------------------------------
# By Daniel Speer
# https://leetcode.com/problems/reverse-nodes-in-k-group/
# Completed 6/8/19
#-------------------------------------------------------------------------------
#    Approach   
#-------------------------------------------------------------------------------

"""
1. Create Dummy node and use as head.
2. Traverse k nodes to verify they exist. 
3. Reverse k nodes in place.
4. Point kth node at the rest of list.
5. Return Dummy.next
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#-------------------------------------------------------------------------------
#    Soluton
#-------------------------------------------------------------------------------

def reverse_k(head: ListNode, k: int) -> ListNode:
    """Reverse nodes in chunks of length k."""
    dummy = ListNode(None)
    dummy.next = head

    def _k_nodes_exist(node: ListNode) -> bool:
        """Return True if k more nodes exist."""
        count = k
        while count > 0 and node:
            node = node.next
            count -= 1
        return type(node) is ListNode

    def _reverse_k(head: ListNode):
        """If k more nodes exist, reverse them in place."""
        if _k_nodes_exist(head):
            new_last_node = head.next
            new_list = None
            count = k
            while count > 0:
                next_node = head.next
                head.next = head.next.next
                next_node.next = new_list
                new_list = next_node
                count -= 1

            new_last_node.next = head.next
            head.next = new_list
            _reverse_k(new_last_node)

    _reverse_k(dummy)
    return dummy.next

#-------------------------------------------------------------------------------
#    Main Leetcode Input Driver
#-------------------------------------------------------------------------------

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """Reverse nodes in chunks of length k.

        Input:
        :head: ListNode -> head of linked list
        :k:    int      -> length of reverse chunk
        
        Output:
        ListNode -> head of k-reversed linked list
        """        
        return reverse_k(head, k)

