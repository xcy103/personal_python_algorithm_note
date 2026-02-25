import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
g = [input().strip() for _ in range(n)]

INF = 10**18
dist = [[INF] * m for _ in range(n)]
dist[0][0] = 0

dq = deque()
dq.append((0, 0))

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while dq:
    x, y = dq.popleft()
    
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < n and 0 <= ny < m:
            cost = 1 if g[nx][ny] == '#' else 0
            
            if dist[nx][ny] > dist[x][y] + cost:
                dist[nx][ny] = dist[x][y] + cost
                
                if cost == 1:
                    dq.append((nx, ny))
                else:
                    dq.appendleft((nx, ny))

print(dist[n-1][m-1])