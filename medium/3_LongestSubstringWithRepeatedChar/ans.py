### LeetCode 3: O(n) time, and O(M) space, M is 128 ASCII char; using sliding window technique to solve

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index_book = {}
        slow = 0
        longest_length = 0

        for index, char in enumerate(s):
            if char in index_book:
                dup_idx = index_book[char]
                if slow <= dup_idx:
                    slow = dup_idx + 1
            index_book[char] = index

            current_length = index - slow + 1
            if current_length > longest_length:
                longest_length = current_length
        
        return longest_length
