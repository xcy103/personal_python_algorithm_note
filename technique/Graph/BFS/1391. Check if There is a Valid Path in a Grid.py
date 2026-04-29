from collections import deque

class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])

        dirs = {
            1: [(0,-1),(0,1)],
            2: [(-1,0),(1,0)],
            3: [(0,-1),(1,0)],
            4: [(0,1),(1,0)],
            5: [(0,-1),(-1,0)],
            6: [(0,1),(-1,0)],
        }

        q = deque([(0,0)])
        vis = set([(0,0)])

        while q:
            x, y = q.popleft()

            if (x,y) == (m-1,n-1):
                return True

            for dx, dy in dirs[grid[x][y]]:
                nx, ny = x+dx, y+dy

                if not (0<=nx<m and 0<=ny<n):
                    continue

                if (nx,ny) in vis:
                    continue

                # 🔥关键：对方也必须能连回来
                if (-dx, -dy) in dirs[grid[nx][ny]]:
                    vis.add((nx,ny))
                    q.append((nx,ny))

        return False