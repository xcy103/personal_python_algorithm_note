#我刚开始自己写的时候，没有在意垃圾需要用mask
#主要就这俩大问题吧，然后后来需要剪枝，不剪枝有概率不能通过
from typing import List
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        classroom = [list(x) for x in classroom]
        m, n = len(classroom), len(classroom[0])

        sx = sy = 0
        lid = {}
        idx = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    sx, sy = i, j
                elif classroom[i][j] == 'L':
                    lid[(i,j)] = idx
                    idx += 1

        litter = idx
        target = (1 << litter) - 1
        best = [[[-1]*(1<<litter) for _ in range(n)] for _ in range(m)]
        best[sx][sy][0] = energy

        q = deque()
        q.append((sx,sy,energy,0))

        steps = 0

        while q:
            for _ in range(len(q)):
                x,y,e,mask = q.popleft()

                if mask == target:
                    return steps
                
                for nx, ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                    if not (0 <= nx < m and 0 <= ny < n):
                        continue
                    if classroom[nx][ny] == 'X':
                        continue
                    
                    ne = e-1
                    if ne<0:
                        continue
                    nmask = mask

                    if (nx,ny) in lid:
                        nmask |= (1 << lid[(nx,ny)])

                    if classroom[nx][ny] == 'R':
                        ne = energy
                    
                    if best[nx][ny][nmask]>=ne:
                        continue
                    best[nx][ny][nmask] = ne
                    q.append((nx, ny, ne, nmask))
            steps+=1
        
        return -1