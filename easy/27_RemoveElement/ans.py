### LeetCode 27: O(n) time, O(1) space(handle in place), using a slow pointer to point at the addr which the ans should be at

from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        if val > 50:
            return length

        slow = 0
        for fast in range(length):
            if nums[fast] != val:
                # Only need to overwrite the front. No need to swap since the back is ignored.
                nums[slow] = nums[fast] 
                slow +=1

        return slow

