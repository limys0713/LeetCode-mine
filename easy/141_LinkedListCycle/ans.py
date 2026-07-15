# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:        
        slow = head
        fast = head
        # If there is no next node then the .next = None, not error, so fast.next.next will never cause error
        # while fast >> also used to check whether head = None(edge case)
        while fast and fast.next:   
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False