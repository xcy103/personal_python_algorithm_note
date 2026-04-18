import sys
from collections import deque
n,m = list(map(int,sys.stdin.readline().split()))
g = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,c = list(map(int,sys.stdin.readline().split()))
    g[u].append((v,c))

dist = [10**18]*(n+1)
dist[1] = 0
q = deque()
q.append((0,1))
while q:
    d,u = q.popleft()
    if d>dist[u]:
        continue
    for v,c in g[u]:
        if dist[v]>d+c:
            dist[v] = d+c
            q.append((d+c,v))
print(dist[n])