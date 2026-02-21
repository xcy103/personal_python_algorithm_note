# 三个点的最近公共祖先，只有一个或者两个
import sys

input = sys.stdin.readline

# 读取
n, m = map(int, input().split())

# 邻接表
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

power = n.bit_length() - 1

deep = [0] * (n + 1)
stjump = [[0]*(power+1) for _ in range(n+1)]

def dfs(u,f):
    deep[u] = deep[f] + 1
    stjump[u][0] = f
    for p in range(1,power+1):
        stjump[u][p] = stjump[stjump[u][p-1]][p-1]
    
    for v in g[u]:
        if v!=f:
            dfs(v,u)

def lca(u,v):
    if deep[u]<deep[v]:
        u,v = v,u
    for p in range(power,-1,-1):
        if deep[stjump[u][p]] >= deep[v]:
            u = stjump[u][p]
    
    if u==v:
        return u
    for p in range(power,-1,-1):
        if stjump[u][p] != stjump[v][p]:
            u = stjump[u][p]
            v = stjump[v][p]
    
    return stjump[u][0]

def compute(a,b,c):
    h1 = lca(a, b)
    h2 = lca(a, c)
    h3 = lca(b, c)

    if h1!=h2:
        if deep[h1]<deep[h2]:
            high = h1
            low = h2
        else:
            high = h2
            low = h1
    else:
        high = h1
        low = h3
    
    togather = low
    cost = deep[a] + deep[b] + deep[c] - deep[high]*2 - deep[low]
    return cost,togather

dfs(1,0)

out = []
for _ in range(m):
    a, b, c = map(int, input().split())
    t, cst = compute(a, b, c)
    out.append(f"{t} {cst}")
print("\n".join(out))