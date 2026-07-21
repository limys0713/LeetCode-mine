### LeetCode 238: O(n) time complex with two O(n) loop, O(1) space with only the list output which is not included in space calculation; using work towwards and backwards method to solve
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        answer = [1] * length # Static space instead of dynamic spacing cuz alrd know the size of the answer
        for index in range(length - 1): # Loop is not include the last index
            # Count the answer of the next index as only one index+1, instead of two index-1
            answer[index + 1] = nums[index] * answer[index]

        right_product = 1
        ### 0~len(nums)-2: Not include the last answer
        for index in range(len(nums)-1, -1, -1): 
            answer[index] *= right_product
            right_product *= nums[index] 

        return answer