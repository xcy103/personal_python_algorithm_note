import sys
import heapq

input = sys.stdin.readline

n, m, t = map(int, input().split())

g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    g[a].append((b, w))
    g[b].append((a, w))

inf = float('inf')
dis = [inf]*(n+1)
dis[1] = 0
q = [(0, 1)]

while q:
    d, u = heapq.heappop(q)
    if d > dis[u]:
        continue
    if u == t:
        break

    for v, w in g[u]:
        if dis[v] > d + w:
            dis[v] = d + w
            heapq.heappush(q, (dis[v], v))

print(dis[t]*2 if dis[t] != inf else -1)