# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        left = 1
        right = n
        while left < right:
            mid = left + ((right - left) // 2)
            bad_quality = isBadVersion(mid)
            if bad_quality:
                right = mid
            else:
                left = mid + 1
        
        return left
  