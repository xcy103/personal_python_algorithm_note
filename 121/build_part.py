MAXN = 300001

g = [[] for _ in range(MAXN)]
father = list(range(MAXN))
dist = [0] * MAXN
dia = [0] * MAXN

def find(x):
    if father[x] != x:
        father[x] = find(father[x])
    return father[x]

def add_edge(u, v):
    g[u].append(v)
    g[v].append(u)

def dp(u,f):
    for v in g[u]:
        if v != f:
            dp(v, u)
    for v in g[u]:
        if v != f:
            dist[u] = max(dist[u], dist[v] + 1)
            dia[u] = max(dia[u], dia[v],dist[u] + dist[v] + 1)

def forest(n):
    for i in range(1, n + 1):
        fu = find(i)
        if fu == i:
            dp(i, 0)

def query(x):
    fx = find(x)
    return dia[fx]

def union(u, v):
    fu = find(u)
    fv = find(v)
    if fu==fv:
        return
    father[fu] = fv
    dia[fv] = max(dia[fu], dia[fv], 
                  (dia[fu]+1)//2 + (dia[fv]+1)//2 + 1)
