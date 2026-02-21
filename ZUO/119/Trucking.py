import sys

input = sys.stdin.readline

# 读入
n, m = map(int, input().split())

edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

father = list(range(n+1))

def find(x):
    while father[x] != x:
        father[x] = father[father[x]]
        x = father[x]
    return x

edges.sort(key=lambda x: -x[2])
g = [[] for _ in range(n + 1)]
# 建树时存权值
for u, v, w in edges:
    fu = find(u)
    fv = find(v)
    if fu != fv:
        father[fu] = fv
        g[u].append((v, w))
        g[v].append((u, w))

# power = 0
# while (1 << power) <= (n >> 1):
#     power += 1
power = n.bit_length()
deep = [0] * (n + 1)
stjump = [[0] * (power + 1) for _ in range(n + 1)]
stmin = [[0] * (power + 1) for _ in range(n + 1)]
vis = [False] * (n + 1)

def dfs(u, w, f):
    vis[u] = True
    deep[u] = deep[f] + 1
    stjump[u][0] = f
    stmin[u][0] = 10**9 if f==0 else w


    for p in range(1, power + 1):
        anc = stjump[u][p - 1]
        stjump[u][p] = stjump[anc][p - 1]
        stmin[u][p] = min(stmin[u][p - 1], stmin[anc][p - 1])

    for v, weight in g[u]:
        if not vis[v]:
            dfs(v, weight, u)

for i in range(1, n + 1):
    if not vis[i]:
        dfs(i, 0, 0)

def query(a, b):
    if find(a) != find(b):
        return -1

    if deep[a] < deep[b]:
        a, b = b, a

    ans = 10**9

    # 拉平
    for p in range(power, -1, -1):
        if deep[stjump[a][p]] >= deep[b]:
            ans = min(ans, stmin[a][p])
            a = stjump[a][p]

    if a == b:
        return ans

    # 同时跳
    for p in range(power, -1, -1):
        if stjump[a][p] != stjump[b][p]:
            ans = min(ans, stmin[a][p], stmin[b][p])
            a = stjump[a][p]
            b = stjump[b][p]

    ans = min(ans, stmin[a][0], stmin[b][0])
    return ans
