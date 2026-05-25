# import sys
# from heapq import heappop,heappush
# mp = {}

# n,m,k = map(int,input().split())

# g = [[] for _ in range(n+1)]

# for _ in range(m):
#     a,b,c = map(int,input().split())
#     g[a].append((b,c))
#     g[b].append((a,c))

# for _ in range(k):
#     l,c = map(int,input().split())
#     mp[l] = c

# dist = [10**18]*(n+1)
# dist[1] = mp.get(1,0)
# h = [([mp.get(1,0),1])]

# while h:
#     d,cur = heappop(h)
#     if d>dist[cur]:continue
#     for nxt,w in g[cur]:
#         toll = mp.get(nxt,0)
#         if dist[nxt] > w+d+toll:
#             dist[nxt] = w+d+toll
#             heappush(h,(w+d+toll,nxt))
# print(dist[n])

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n, m, k = map(int, input().split())

g = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

mp = {}
for _ in range(k):
    l, c = map(int, input().split())
    mp[l] = c

INF = 10**18
dist = [INF]*(n+1)

# ✅ 起点统一
dist[1] = mp.get(1, 0)
h = [(dist[1], 1)]

while h:
    d, cur = heappop(h)

    # ✅ 关键剪枝（必须有）
    if d > dist[cur]:
        continue

    for nxt, w in g[cur]:
        nd = d + w + mp.get(nxt, 0)
        if dist[nxt] > nd:
            dist[nxt] = nd
            heappush(h, (nd, nxt))

print(dist[n])