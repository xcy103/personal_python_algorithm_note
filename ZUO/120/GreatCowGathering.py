# 树的重心之和点权有关，边权怎么分布无所谓
import sys

input = sys.stdin.readline

n = int(input())

# 每个点的牛数量（1-index）
cow = [0] + list(map(int, input().split()))

g = [[] for _ in range(n+1)]

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    g[u].append((v, w))
    g[v].append((u, w))

# 牛的总数
cowSum = sum(cow)

# size[i]：以 i 为根的子树牛总量
size = [0] * (n + 1)

best = float('inf')
center = 0

def find_center(u,f):
    global center, best
    for v in g[u]:
        if v!=f:
            find_center(v, u)
            size[u]+=size[v]
            max_sub = max(max_sub, size[v])
    
    max_sub = max(max_sub, cowSum - size[u])
    if max_sub < best:
        best = max_sub
        center = u

path = [0]*(n+1)

def set_path(u,f):
    for v,w in g[u]:
        if v!=f:
            path[v] = path[u] + w
            set_path(v, u)

find_center(1, 0)

path[center] = 0
set_path(center, 0)

ans = 0
for i in range(1, n + 1):
    ans += cow[i] * path[i]

print(ans)