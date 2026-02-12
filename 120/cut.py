n = int(input())
g = []
size = []
maxsub = []

centers = []

leaf = 0
leafather = 0

def build():
    global g,size,maxsub
    g = [[] for _ in range(n+1)]
    size = [0]*(n+1)
    maxsub = [0]*(n+1)

def add_edge(u, v):
    g[u].append(v)
    g[v].append(u)

def dfs(u, f):
    size[u] = 1
    maxsub[u] = 0
    for v in g[u]:
        if v == f:
            continue
        dfs(v, u)
        size[u] += size[v]
        maxsub[u] = max(maxsub[u], size[v])
    maxsub[u] = max(maxsub[u], n - size[u])

def get_center():
    global centers
    h = n//2
    for i in range(1, n+1):
        if maxsub[i] <= h:
            centers.append(i)
    return len(centers)

def get_leaf(u,f):
    for v in g[u]:
        if v == f:
            continue
        get_leaf(v, u)
        return 
    leaf = u
    leafather = f

def solve():
    dfs(1, 0)
    get_center()
    if len(centers) == 1:
        c = centers[0]
        v = g[c][0]
        return (c, v), (v, c)
        
    else:
        get_leaf(centers[1], centers[0])
        return (leafather, leaf), (centers[0], leaf)