from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        slow_ptr = -1 # num after this index is zero

        # index also acts as the whose turn variable
        for index in range(len(nums)):
            if nums[index] != 0:
                slow_ptr +=1
                if (index - slow_ptr) != 0:
                    nums[slow_ptr] = nums[index]
                    nums[index] = 0
            
        