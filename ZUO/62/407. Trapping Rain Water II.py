
# 先把四周边界加入最小堆，作为初始“围墙”。
# 每次弹出当前最低的边界高度 h。
# 这个点能接的水 = h - 自身高度。
# 向四周扩展，邻居的新水位 = max(h, 邻居高度)。
# 重复直到堆空。
# 用最小堆从外向内“灌水”，h 表示当前水位，不是原始高度。
from heapq import heappush,heappop
from typing import List
class Solution:
    def trapRainWater(self, height: List[List[int]]) -> int:
        if not height or not height[0]:
            return 0
        
        m,n = len(height),len(height[0])

        heap = []
        vis = [[False]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i==0 or i==m-1 or j==0 or j==n-1:
                    heappush(heap,(height[i][j],i,j))
                    vis[i][j] = True
        ans = 0
        while heap:
            h,i,j = heappop(heap)
            ans+=h-height[i][j]
            for ni,nj in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
                if 0<=ni<m and 0<=nj<n and not vis[ni][nj]:
                    heappush(heap,(max(h,height[ni][nj]),ni,nj))
                    vis[ni][nj] = True
        return ans