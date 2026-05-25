#枚举“已覆盖的设施集合（mask）”，用 DP 转移：对每个公司更新 mask | cover[i] 的最小成本。
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

cost = list(map(int, input().split()))

cover = []
for _ in range(n):
    row = list(map(int, input().split()))
    mask = 0
    for j in range(m):
        if row[j]:
            mask |= (1 << j)
    cover.append(mask)

INF = 10**18
dp = [INF] * (1 << m)
dp[0] = 0

for i in range(n):
    c = cost[i]
    cmask = cover[i]

    for mask in range(1<<m):
        if dp[mask]==INF:continue

        nmask = mask | cmask
        if dp[nmask] > dp[mask] + c:
            dp[nmask] = dp[mask] + c  

ans = dp[(1 << m) - 1]
print(ans if ans < INF else -1)