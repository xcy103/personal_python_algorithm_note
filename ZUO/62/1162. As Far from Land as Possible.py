# 多源BFS
# 思路就是把所有陆地进队列，然后开始拓展，
# 拓展一次就是多一层，当所有点遍历完了，最后的层数-1就是答案
from collections import deque
from typing import List

class Solution:
    def maxDistance(self, g: List[List[int]]) -> int:
        n = len(g)
        q = deque()
        vis = [[False]*n for _ in range(n)]

        seas = 0
        for i in range(n):
            for j in range(n):
                if g[i][j]==1:
                    q.append((i,j))
                    vis[i][j]==True
                else:
                    seas+=1
        if seas==0 or seas==n*n:
            return -1
        
        l=0
        while q:
            l+=1
            size = len(q)
            for _ in range(size):
                x,y = q.popleft()
                for (nx,ny) in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
                    if 0<=nx<n and 0<=ny<n and not vis[nx][ny]:
                        vis[nx][ny]=True
                        q.append((nx,ny))
        return l-1