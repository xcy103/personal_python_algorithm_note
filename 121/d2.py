#树形dp求树的直径，缺点是无法找到直径的路径


from math import inf


MAXN = 50001

g = [[] for _ in range(MAXN)]

dist = [0] * MAXN
d = -inf

def add_edge(u, v, w):
    g[u].append([v, w])
    g[v].append([u, w])

def dp(u,f):
    global d

    for v, w in g[u]:
        if v !=f:
            dp(v, u)

    for v,w in g[u]:
        if v != f:
            d = max(d, dist[u] + dist[v] + w)
            dist[u] = max(dist[u], dist[v] + w)