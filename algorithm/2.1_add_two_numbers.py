# Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/
# Completed 5/6/19

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, list1: ListNode, list2: ListNode) -> ListNode:
        return self.list_sum(list1, list2)

    def list_sum(
            self,
            list1: ListNode,
            list2: ListNode,
            carryover: int = 0,
            last_node: ListNode = None
    ) -> ListNode:
        """Return the sum of two numbers. Numbers are stored in linked list in reverse order.
        
        Input:
        :list1: ListNode -- root node to first number's linked list
        :list2: ListNode -- root node to second number's linked list

        Output:
        ListNode -- root node to sum of input numbers.
        """
        current_sum = self.node_sum(list1, list2, carryover)
        if not last_node:
            next_node = ListNode(current_sum % 10)
        else:
            next_node = ListNode(current_sum % 10)
            last_node.next = next_node

        if list1: list1 = list1.next
        if list2: list2 = list2.next
            
        if list1 or list2 or current_sum // 10 > 0:
            self.list_sum(list1, list2, current_sum // 10, next_node)
        return next_node

    def node_sum(self, list1: ListNode, list2: ListNode, carryover: int) -> int:
        """Return sum of input nodes and carryover"""
        total = carryover
        if list1: total += list1.val
        if list2: total += list2.val
        return total
        
        
        
