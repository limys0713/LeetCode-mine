class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:   # Empty string guard
            return -1

        # --- Space Complexity: strictly O(1) ---
        # Fixed 26-slot array representing the English alphabet. 
        # (中文輔助：嚴格 O(1) 空間。固定 26 格陣列，完全避開 Hash Map 的記憶體與雜湊開銷。)
        
        # State Machine Definitions (狀態機定義):
        #  -1 : Never seen (從未見過)
        # >=0 : Seen exactly once at this index (只出現過一次，記錄其原字串中的 Index)
        #  -2 : Duplicate / Dead (出現兩次以上，徹底淘汰)
        freq_list = [-1] * 26
        
        # --- Pass 1: Build the State Machine ---
        # Time Complexity: O(N) - N is the length of the string 's'
        for index, char in enumerate(s):
            ascii_value = ord(char) - 97
            
            if freq_list[ascii_value] == -1:
                freq_list[ascii_value] = index  # State transition to "Seen Once"
            else:
                freq_list[ascii_value] = -2     # State transition to "Dead"
        
        # --- Pass 2: Find the First Unique Character ---
        # Time Complexity: O(1) - Maximum 26 iterations (O(26)), regardless of string length N
        min_index = float('inf')  # Initialize with IEEE 754 Infinity
        
        # Loop through the 26 slots. We want the SMALLEST valid index.
        # (中文輔助：掃描 26 格。只要狀態 >= 0，代表它是唯一的。我們從中挑出數字最小的，也就是最先出現的字母位置。)
        for index_value in freq_list:
            if index_value >= 0:
                min_index = min(min_index, index_value)

        # If min_index is still infinity, no unique character exists
        if min_index == float('inf'):
            return -1
        
        return min_index