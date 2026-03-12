#发现自己总是想复杂，这道题用一个used集合判断就行
#其次是自己不应该在来到下一个字母前判断是不是字母，来到这个数字再说

from typing import List
from collections import deque
class Solution:
    def minMoves(self, mat: List[str]) -> int:
        mat = [list(x) for x in mat]
        m,n = len(mat),len(mat[0])
        d = defaultdict(list)
        
        for i in range(m):
            for j in range(n):
                if mat[i][j].isalpha():
                    d[mat[i][j]].append((i,j))
        
        used = set()
        q = deque()
        q.append((0,0))
        dist = [[inf]*n for _ in range(m)]
        dist[0][0]=0

        while q:
            x,y = q.popleft()
            step = dist[x][y]
            if (x,y)==(m-1,n-1):
                return step
            # 四方向
            for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if not (0<=nx<m and 0<=ny<n):
                    continue
                if mat[nx][ny] == '#':
                    continue
                if dist[nx][ny] <= step+1:
                    continue

                dist[nx][ny] = step+1
                q.append((nx,ny))
            
            if mat[x][y].isalpha() and mat[x][y] not in used:
                used.add(mat[x][y])

                for nx,ny in d[mat[x][y]]:
                    if dist[nx][ny]<=step:
                        continue
                    
                    dist[nx][ny] = step
                    q.appendleft((nx,ny))

                d[mat[x][y]].clear()

        return -1
            
