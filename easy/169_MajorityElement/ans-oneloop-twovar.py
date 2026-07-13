from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        # Boyer-Moore Voting Algorithm
        # Core idea: 1-vs-1 cancellation. 
        # The majority element will always survive because it appears more than N/2 times.
        candidate = 0
        count = 0
        
        for num in nums:
            if candidate == num:
                # Ally found: increase health
                count += 1
            else:
                if count == 0:
                    # Empty arena: new candidate claims the throne
                    candidate = num
                    count += 1
                else:
                    # Enemy found: mutual destruction
                    count -= 1

        return candidate