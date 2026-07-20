### LeetCode 56: Time: O(nlogn) in sorting + O(n) in checking intervals, Space: O(n); sort first then solve
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])
        ans = []
        ans.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] > ans[-1][1]:
                ans.append(intervals[i])
            else: # interval[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])

        return ans