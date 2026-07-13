class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # --- WHY LIST OVER PRE-FILLED DICT? (资深面试标准回答) ---
        # 1. Fixed Domain (固定范围): 
        #    The problem limits inputs strictly to 26 lowercase letters.
        #    (中文辅助：题目限定了只有 26 个小写字母，范围死死固定。)
        
        # 2. Lookup Overhead (寻址开销对决): 
        #    Array uses raw pointer arithmetic (Base Address + Offset). 
        #    Dictionaries must compute Hashes and handle potential collisions even if pre-filled.
        #    (中文辅助：阵列底层使用极速的“基址 + 偏移量”指针数学寻址。而字典即使预先建好，每次找字母还是得跑完一整套耗时的哈希数学运算。)
        
        # 3. Memory Footprint (内存虚胖): 
        #    An array stores exactly 26 integers. 
        #    A dictionary stores Keys, Values, Hash codes, and requires empty padding (Load Factor) to function.
        #    (中文辅助：阵列只存 26 个纯数字，极致干净。字典为了维持运作，必须同时存下钥匙、值、哈希码，还要刻意留一堆空位，造成严重的内存虚胖。)
        
        # List initialization: [] in python
        frequency_map = [0] * 26

        # ord() function: convert char to ascii code
        for char_s, char_t in zip(s, t):    # zip: for pairing
            frequency_map[ord(char_s) - 97] += 1
            frequency_map[ord(char_t) - 97] -= 1

        # Compare with array 
        return frequency_map == [0] * 26