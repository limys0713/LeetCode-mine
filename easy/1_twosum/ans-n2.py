class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # List in python: []
        # In python, there is no need to write the var type
        #ans = []
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):    ### Can loop from i+1, therefore no need to check the i==j condition statement + the complexity will lower than O(n^2)
                # if i==j:
                #     continue
                temp = nums[i] + nums[j]
                if(temp == target): return [i, j]   # Because there is only one valid answer
                    #ans.append([i, j])   # need [i,j] (array) if wanna append more than one element at a time
        #return ans
        