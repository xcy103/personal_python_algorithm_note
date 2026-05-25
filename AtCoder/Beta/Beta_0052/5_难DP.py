#哎太难，这个状态定义
#dp[mask][u] = 到达 u，访问过 mask，最大剩余体力
import heapq

n, m, F = map(int, input().split())
R = list(map(int, input().split()))

g = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append((v, w))
    g[v].append((u, w))

INF = -1
dp = [[INF]*n for _ in range(1<<n)]

start = 1<<0
dp[start][0] = F + R[0]

pq = [(-(F + R[0]), start, 0)]  # max heap

while pq:
    neg, mask, u = heapq.heappop(pq)
    cur = -neg

    if dp[mask][u] > cur:
        continue

    for v, w in g[u]:
        if cur < w:
            continue

        new = cur - w
        new_mask = mask

        if not (mask >> v & 1):
            new += R[v]
            new_mask |= (1<<v)

        if dp[new_mask][v] < new:
            dp[new_mask][v] = new
            heapq.heappush(pq, (-new, new_mask, v))

ans = -1
for mask in range(1<<n):
    ans = max(ans, dp[mask][n-1])

print(ans if ans >= 0 else -1)