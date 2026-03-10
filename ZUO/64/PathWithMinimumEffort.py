#我是笨蛋。。。这道题不是纯粹模板，dis表定义为到则这个点路径差值绝对值的最大值
#从堆里弹出来一个，然后求他到周围节点的差值，如果差值变小，就更新
from heapq import *
from math import inf
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m,n = len(heights),len(heights[0])

        dis = [[inf]*n for _ in range(m)]
        dis[0][0] = 0

        h = [(0,0,0)]

        while h:
            w,x,y = heappop(h)

            if (x,y) == (m-1,n-1):
                return w
            
            if w > dis[x][y]:
                continue
            
            for nx,ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                if 0<=nx<m and 0<=ny<n:
                    new = max(w, abs(heights[x][y]-heights[nx][ny]))
                    if new < dis[nx][ny]:
                        dis[nx][ny] = new
                        heappush(h,(new,nx,ny))

        return 0