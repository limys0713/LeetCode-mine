class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary in python: {}
        seen = {}
        length = len(nums)
        for i in range(length):
            complement = target - nums[i]
            if complement not in seen:
                seen[nums[i]] = i
            else:
                return [seen[complement], i]