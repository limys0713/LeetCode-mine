### LeetCode 179: O(n log n) time, O(n) space(string array and answer string), using a custom comparator to sort strings by comparing front+back and back+front

from functools import cmp_to_key
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # O(N) Time & Space: Convert integers to strings
        strings = [str(num) for num in nums]
        
        # O(N log N) Time: Sort using custom lexicographical rule
        strings.sort(key=cmp_to_key(self.compare))
        
        # O(N) Time & Space: Concatenate all strings
        answer = "".join(strings)
        
        # O(1) Time: Handle edge case where array has only zeroes (e.g., [0, 0])
        if answer[0] == "0":
            return "0"
            
        return answer

    def compare(self, front: str, back: str) -> int:
        # Lexicographical comparison without int() overhead (Compare string (Using ascii dict sequence to compare))
        if (front + back) < (back + front):
            return 1  # if back is larger, need to receive false, >>  1 < 0 => False means swaps
        else:
            return -1