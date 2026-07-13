class Solution:
    def isPalindrome(self, s: str) -> bool:

        if s is None:   # s does not exist, excluding empty string ""
            return False
        
        left = 0 
        right = len(s) - 1
        while right > left:
            while right > left and not s[left].isalnum():
                left +=1
            while right > left and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -=1

        return True