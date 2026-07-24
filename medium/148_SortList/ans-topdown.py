### LeetCode 148: O(nlogn)time, O(n)space for call stack; using recursive which is top-down approach to solve

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        # Divide
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None # Cut the list
        
        left_sorted = self.sortList(head)
        right_sorted= self.sortList(mid)

        # Sort & Merge
        dummy = ListNode()
        curr = dummy

        while left_sorted and right_sorted:
            if left_sorted.val <= right_sorted.val:
                curr.next = left_sorted
                curr = curr.next
                left_sorted = left_sorted.next
            else:
                curr.next = right_sorted
                curr = curr.next
                right_sorted = right_sorted.next
        
        curr.next = left_sorted or right_sorted
        
        return dummy.next