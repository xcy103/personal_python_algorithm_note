import sys
from heapq import heapify,heappop,heappush

n,m,k = list(map(int,sys.stdin.readline().split()))
g = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,w = list(map(int,sys.stdin.readline().split()))
    if w<k:continue
    g[u].append(v)
    g[v].append(u)
INF = 10**18
dist = [INF]*(n+1)
dist[1] = 0
h = [(0,1)]
while h:
    d,u = heappop(h)
    if dist[u]<d:continue
    for v in g[u]:
        if dist[v]>d+1:
            dist[v] = d+1
            heappush(h,(d+1,v))
ans = -1 if dist[n]==INF else dist[n]
print(ans)