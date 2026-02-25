from bisect import bisect_left
from type import List
#利用二分优化，对于结束时间进行排序
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x:x[1])
        n = len(events)
        dp = [[0]*(k+1) for _ in range(n)]
        ends = [e[1] for e in events]
        for i in range(1,k+1):
            dp[0][i] = events[0][2]

        for i in range(1,n):
            start = events[i][0]
            pre = bisect_left(ends,start)-1

            for j in range(1,k+1):
                c1 = dp[i-1][j]

                c2 = events[i][2]
                if pre>=0:
                    c2+=dp[pre][j-1]
                dp[i][j] = max(c1,c2)
        return dp[-1][-1]