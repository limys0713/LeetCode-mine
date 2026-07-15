from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid_num = left + ((right - left) // 2)
            if nums[mid_num] == target:
                return mid_num
            elif nums[mid_num] > target:
                right = mid_num - 1
            else:
                left = mid_num + 1

        return -1