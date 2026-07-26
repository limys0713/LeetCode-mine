### LeetCode 148: O(nlogn)time, O(1)space including call stack; using bottom-up approach to solve

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.sort_merge_dummy = ListNode(val=0)

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        length = 0
        curr = head
        while curr:
            length +=1
            curr = curr.next

        steps = 1
        dummy = ListNode(val=0)
        dummy.next = head
        while steps < length:
            prev = dummy
            curr = dummy.next   # Set the current to the first node
            while curr:
                left_list = curr
                right_list = self.split(curr, steps)
                
                curr = self.split(right_list, steps)

                # Link the sorted result to the previous chain 
                # Change the prev to the last node of the sorted result
                prev.next, prev = self.sort_and_merge(left_list, right_list)
                # Actually, there is no need to Link the list back
                # prev.next = curr
            
            steps *=2

        return dummy.next
    
    def split(self, head: Optional[ListNode], steps: int) -> Optional[ListNode]:
        if head is None:
            return head

        step = 1
        curr = head
        while curr.next and step < steps:
            curr = curr.next
            step +=1
        remaining = curr.next
        curr.next = None # cut the line

        return remaining

    def sort_and_merge(self, left_list: Optional[ListNode], right_list: Optional[ListNode]) -> Tuple[ListNode, ListNode]:

        ans = self.sort_merge_dummy
        while left_list and right_list:
            if left_list.val <= right_list.val:
                ans.next = left_list
                left_list = left_list.next
            else:
                ans.next = right_list
                right_list = right_list.next
            ans = ans.next
        
        ans.next = left_list or right_list
        while ans.next: # Locate the last node of the sorted list
            ans = ans.next

        return self.sort_merge_dummy.next, ans
        