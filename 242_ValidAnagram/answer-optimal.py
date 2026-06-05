class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # List initialization: [] in python
        frequency_map = [0] * 26

        # ord() function: convert char to ascii code
        for char in s:    # zip: for pairing
            frequency_map[ord(char) - 97] += 1
        
        for char in t:
            frequency_map[ord(char) - 97] -= 1

        # Compare with array 
        return frequency_map == [0] * 26