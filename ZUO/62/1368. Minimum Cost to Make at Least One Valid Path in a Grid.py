#还是经典的01bfs，只不过判断权值变成了
# 判断箭头方向和我要去的方向是否一致，其实还是01bfs
# 因为我要先试试和箭头一直的方向的路径
# 不行了在尝试有代价的路径方向
#01bfs过程，有dis表
#首先源头加入队列，同时改源点dis为0
#接着从队列弹出节点，处理这个节点所有的边，如果边权是1，从尾巴进入，0则从头进入，
#这一步i相当于修正，距离，比如这个 a到b,c分别有一条1的边，b,c到目标点d，分别有一条1，0的边
#我们先处理b，b把d从队尾进入，但这个是不对的，因为边权大，我们接着处理c,通过c把d从头进入
#这一步相当于修正了，把更小的距离安排在优先弹出的位置，合理，如果后面再遇到弹出的点
#如果距离大于dis表中的距离，我们可以直接忽略

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