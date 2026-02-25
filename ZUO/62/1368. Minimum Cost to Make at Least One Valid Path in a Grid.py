#还是经典的01bfs，只不过判断权值变成了
# 判断箭头方向和我要去的方向是否一致，其实还是01bfs
# 因为我要先试试和箭头一直的方向的路径
# 不行了在尝试有代价的路径方向


from collections import deque
from math import inf
from typing import List
class Solution:
    def minCost(self, g: List[List[int]]) -> int:
        m, n = len(g), len(g[0])
        
        q = deque([(0, 0)])
        dis = [[inf] * n for _ in range(m)]
        dis[0][0] = 0
        
        # 右 左 下 上
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while q:
            x, y = q.popleft()
            
            for i, (dx, dy) in enumerate(dirs):
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n:
                    
                    # 如果方向和当前格子箭头一致 cost=0
                    c = 0 if g[x][y] == i + 1 else 1
                    
                    if dis[nx][ny] > dis[x][y] + c:
                        dis[nx][ny] = dis[x][y] + c
                        
                        if c == 0:
                            q.appendleft((nx, ny))
                        else:
                            q.append((nx, ny))
        
        return dis[m-1][n-1]