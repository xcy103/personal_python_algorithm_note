import sys
from heapq import heappush,heappop
n,m,k = list(map(int,sys.stdin.readline().split()))
g = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,c = list(map(int,sys.stdin.readline().split()))
    g[u].append((v,c))
    g[v].append((u,c))
inf = 10**18
dist = [inf]*(n+1)
dist[1] = 0
h = [(0,1)]
while h:
    d,u = heappop(h)
    if dist[u]<d:continue

    for v,c in g[u]:
        if dist[v]>d+c:
            dist[v] = d+c
            heappush(h,(dist[v],v))
print(-1 if dist[n]>k else dist[n])
