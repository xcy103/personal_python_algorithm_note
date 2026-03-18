#先按照结束时间排序，然后除掉有重叠的
#再安排下一个会议，最后长度减去这些安排好的

class Solution:
    def eraseOverlapIntervals(self, times: List[List[int]]) -> int:
        ans = 0
        times.sort(key = lambda x:x[1])
        i = 0
        n = len(times)
        op  = 0
        while i<n:
            cur = times[i][1]
            op+=1
            j = i+1
            while j<n and times[j][0]<cur:
                j+=1
            i = j
        return n-op