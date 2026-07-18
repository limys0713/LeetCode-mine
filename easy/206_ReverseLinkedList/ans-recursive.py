# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

### LeetCode 206: O(n) time and O(n) space(call stack space), using recursive method to solve

from typing import Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        last_node = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return last_node
