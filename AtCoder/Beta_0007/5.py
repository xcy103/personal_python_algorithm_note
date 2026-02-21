import sys
from functools import lru_cache

input = sys.stdin.readline

N, M = map(int, input().split())
S, T = map(int, input().split())

if M > 0:
    P = list(map(int, input().split()))
else:
    P = []

def to_coord(x):
    x -= 1
    return x // N, x % N

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

S = to_coord(S)
T = to_coord(T)
P = [to_coord(x) for x in P]

# 特殊情况
if M == 0:
    print(dist(S, T))
    exit()

@lru_cache(None)
def dfs(mask, last):
    # 所有货架访问完
    if mask == (1<<M) - 1:
        return dist(P[last], T)

    ans = float('inf')

    for nxt in range(M):
        if mask & (1<<nxt):
            continue
        
        new_mask = mask | (1<<nxt)
        ans = min(
            ans,
            dist(P[last], P[nxt]) +
            dfs(new_mask, nxt)
        )

    return ans


# 从 S 出发，选第一个货架
ans = float('inf')

for i in range(M):
    ans = min(
        ans,
        dist(S, P[i]) +
        dfs(1<<i, i)
    )

print(ans)