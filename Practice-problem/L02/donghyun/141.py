#!/usr/bin/env python3

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        parent = set()

        current = head
        while current is not None:
            if current.next in parent:
                return True
            parent.add(current.next)
            current = current.next
        return False
