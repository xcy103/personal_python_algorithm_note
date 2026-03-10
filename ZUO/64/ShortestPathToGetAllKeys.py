#bfs结合分层图最短路。。状态判断有点复杂，容易写错
from collections import deque
from typing import List
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        grid = [list(s) for s in grid]
        #vis数组用来记录是否访问过
        vis = [[[False]*(1<<6) for _ in range(31)] for _ in range(31)]
        q = deque()
        m,n = len(grid),len(grid[0])
        mask = 0
        #记录最后的成功状态，以及开始位置
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='@':
                    q.append((i,j,0))
                if 'a'<=grid[i][j]<='f':
                    mask|=1<<(ord(grid[i][j]) - ord('a'))
        level = 1
        while q:
            for _ in range(len(q)):
                x,y,s = q.popleft()
                #向四周阔散，遇到不合法状态返回，遇到钥匙收集，更新状态
                #进入队列
                for nx,ny in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
                    ns = s
                    if nx<0 or nx==m or ny<0 or ny==n or grid[nx][ny]=='#':continue
                    if 'A'<=grid[nx][ny]<='F' and ((ns&(1<<(ord(grid[nx][ny])-ord('A'))))==0):continue
                    if 'a'<=grid[nx][ny]<='f':
                        ns|=1<<(ord(grid[nx][ny])-ord('a'))
                    if ns==mask:
                        return level
                    if not vis[nx][ny][ns]:
                        vis[nx][ny][ns] = True
                        q.append((nx,ny,ns))
            level+=1
        return -1