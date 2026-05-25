import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n, m, k, t = map(int, input().split())

g = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

mp = set(list(map(int,input().split())))

INF = 10**18
dist = [INF]*(n+1)

# ✅ 起点统一
dist[1] = t if 1 in mp else 0
h = [(dist[1], 1)]

while h:
    d, cur = heappop(h)

    # ✅ 关键剪枝（必须有）
    if d > dist[cur]:
        continue

    for nxt, w in g[cur]:
        nd = d + w + (t if nxt in mp else 0)
        if dist[nxt] > nd:
            dist[nxt] = nd
            heappush(h, (nd, nxt))

print(dist[n])