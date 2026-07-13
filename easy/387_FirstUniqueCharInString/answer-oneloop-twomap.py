class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:   # Empty string or string does not exist
            return -1

        # From python 3.7, hash map will retain the insertion order (like Java LinkedHashMap)
        # Space Complexity: O(1) - Maximum 26 keys for English lowercase letters
        char_index = {} 
        char_amount = {}
        
        # Pass 1: Build the data maps
        # Time Complexity: O(N) - N is the length of the string 's'
        for index, char in enumerate(s):
            if char not in char_amount:
                char_index[char] = index
                char_amount[char] = 1
            else:
                char_amount[char] += 1
        
        # Pass 2: Find the first unique character
        # Time Complexity: O(1) - Maximum 26 iterations (O(26)), regardless of string length N
        # Return the index of the first char that the amount in char_amount is 1
        for char, amount in char_amount.items():
            if amount == 1:
                return char_index[char]
        
        return -1