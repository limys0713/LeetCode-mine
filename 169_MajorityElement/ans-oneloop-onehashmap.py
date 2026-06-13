from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
    
        freq_map = {} # O(n) space (n/2 space actually)
        target = len(nums) // 2 # Only give integer answer
        for num in nums: # O(n) time
            ### Improve from if ... else statement to dict.get(index, 0)
            freq_map[num] = freq_map.get(num, 0) + 1
            if freq_map[num] > target:
                return num