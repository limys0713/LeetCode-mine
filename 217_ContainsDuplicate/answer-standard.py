from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        # set class in python (hashmap without key)
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False