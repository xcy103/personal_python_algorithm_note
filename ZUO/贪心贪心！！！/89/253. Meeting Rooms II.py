#线段最大重合条数问题
from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # 按开始时间排序
        intervals.sort(key=lambda x: x[0])
        
        heap = []  # 小根堆，存结束时间
        ans = 0
        
        for start, end in intervals:
            # 释放已经结束的会议室
            while heap and heap[0] <= start:
                heapq.heappop(heap)
            
            # 分配新会议室
            heapq.heappush(heap, end)
            
            # 更新最大值
            ans = max(ans, len(heap))
        
        return ans