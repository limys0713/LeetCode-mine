### LeetCode 75: O(n) time, O(1) space(in-place pointers), using three pointers(slow, front, back) to partition the array by swapping 0s to the left and 2s to the right in a single pass

from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(1) space
        slow = 0
        front = 0
        back = len(nums) - 1
        while front <= back: # O(n) time
            if nums[front] == 0:
                nums[slow], nums[front] = nums[front], nums[slow]
                slow +=1
                front +=1
            elif nums[front] == 2:
                nums[back], nums[front] = nums[front], nums[back]
                back -=1
            else:
                front +=1