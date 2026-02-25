#经典01bfs，其实本质上还是dijkstra，不过使用了双端队列替代最小堆
#从开始点出发，向四周拓展，权值为0的从头入队，1的从尾
#道理也很简单，因为0的权值小，可以刷新dis，变小，所以要先处理


from collections import deque
from math import inf
from typing import List
class Solution:
    def minimumObstacles(self, g: List[List[int]]) -> int:
        m = len(g)
        n = len(g[0])

        q = deque([(0, 0)])   # 修正这里
        dis = [[inf]*n for _ in range(m)]
        dis[0][0] = 0
        
        while q:
            x, y = q.popleft()
            if x == m-1 and y == n-1:
                return dis[x][y]

            for nx, ny in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
                if 0 <= nx < m and 0 <= ny < n:
                    c = g[nx][ny]
                    if dis[nx][ny] > dis[x][y] + c:
                        dis[nx][ny] = dis[x][y] + c
                        if c == 0:
                            q.appendleft((nx,ny))
                        else:
                            q.append((nx,ny))
        return -1