#  首先生成最大生成树
#  给的数据可能会有几个集团，每个集团都要生成最大生成树


MAXN = 10001
MAXM = 50001

LOG = 0

edges = []
father = []
vis = []
g = []
stjump = []
stmin = []

def log2(n):
    ans = 0
    while (1 << ans) <= n>>1:
        ans += 1
    return ans

def build(n):
    global LOG, edges, father, vis, g, stjump, stmin

    LOG = log2(n) + 1
    father = [i for i in range(n + 1)]
    vis = [False] * (n + 1)
    g = [[] for _ in range(n + 1)]
    deep = [0] * (n + 1)
    stjump = [[0] * LOG for _ in range(n + 1)]
    stmin = [[inf] * LOG for _ in range(n + 1)]


def find(x):
    if father[x] != x:
        father[x] = find(father[x])
    return father[x]

def kruskal(n):
    edges.sort(key=lambda x: x[2], reverse=True)
    for u, v, w in edges:
        fu = find(u)
        fv = find(v)
        if fu != fv:
            father[fu] = fv
            g[u].append((v, w))
            g[v].append((u, w))

def dfs(u,w,f):
    vis[u] = True
    if f==0:
        deep[u] = 1
        stjump[u][0] = u
        stmin[u][0] = inf
    else:
        deep[u] = deep[f] + 1
        stjump[u][0] = f
        stmin[u][0] = w
    for p in range(1, LOG):
        stjump[u][p] = stjump[stjump[u][p-1]][p-1]
        stmin[u][p] = min(stmin[u][p-1], stmin[stjump[u][p-1]][p-1])
    for v, w2 in g[u]:
        if not vis[v]:
            dfs(v,w2,u)
    
def query(a,b):
    if find(a) != find(b):
        return -1
    if deep[a] < deep[b]:
        a, b = b, a
    ans = inf
    for p in range(LOG - 1, -1, -1):
        if deep[stjump[a][p]] >= deep[b]:
            ans = min(ans, stmin[a][p])
            a = stjump[a][p]
    
    if a == b:
        return ans
    for p in range(LOG - 1, -1, -1):
        if parent[a][p] != parent[b][p]:
            ans = min(ans, min(stmin[a][p], stmin[b][p]))
            a = parent[a][p]
            b = parent[b][p]
    return min(ans, min(stmin[a][0], stmin[b][0]))