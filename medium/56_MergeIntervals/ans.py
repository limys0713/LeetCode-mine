### LeetCode 56: Time: O(nlogn) in sorting + O(n) in checking intervals, Space: O(n); sort first then solve
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])
        ans = []
        ans.append(intervals[0])
        for interval in intervals:
            if interval[0] > ans[-1][1]:
                ans.append(interval)
            else: # interval[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], interval[1])
                ### If wanna improve performace, use code below instead
                """
                if interval[1] > ans[-1][1]:
                    ans[-1][1] = interval[1]
                """

        return ans