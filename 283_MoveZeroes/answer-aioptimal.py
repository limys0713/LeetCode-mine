from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # 直接從 0 開始，定義明確：「下一個準備放非零數字的空位」 << 重點
        slow = 0 
        
        for fast in range(len(nums)):
            if nums[fast] != 0:
                # Python 專屬大絕招：一行無腦交換
                nums[slow], nums[fast] = nums[fast], nums[slow]
                # 換完之後，慢指標往前走一格，準備迎接下一個
                slow += 1