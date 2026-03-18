#这道题就是懒删除堆
#扫描，先按照开始时间排序
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        h = []
        times = 0
        events.sort()
        s = events[0][0]+1
        j = 1
        op = 1
        n = len(events)
        for i in range(1,10**5+1):
            while j<n and events[j][0]<=s:
                heappush(h,events[j][1])
                j+=1
            while h and h[0]<s:
                heappop(h)
            if h:
                heappop(h)
                op+=1
            s+=1
        return op