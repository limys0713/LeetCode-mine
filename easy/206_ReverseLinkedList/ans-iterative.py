# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

### LeetCode 206: O(n) time and O(1) space, using iterative method to solve
from typing import Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        # If current head is None, which means the previous node is the last node
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node

        return prev