from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds the indices of two numbers in the array that add up to the target.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # Edge case: If the list has fewer than 2 items, finding a pair is impossible.
        if not nums or len(nums) < 2:
            return []
            
        seen = {}
        
        # 'enumerate' provides both the index 'i' and the value 'num' simultaneously
        for i, num in enumerate(nums):
            complement = target - num
            
            # O(1) existence check
            if complement in seen:
                return [seen[complement], i]
                
            # Store the number and its index if no match is found yet
            seen[num] = i
            
        # Return empty list if no valid pair exists (Enterprise safety net)
        return []