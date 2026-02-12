#第一种方式求树的直径
#两次dfs，缺点是无法处理有复数边的情况


MAXN = 50001

n = 0
g = [[] for _ in range(MAXN)]

dist = [0] * MAXN
last = [0] * MAXN

start = 0
end = 0
d = 0

def add_edge(u, v, w):
    g[u].append((v, w))
    g[v].append((u, w))

def dfs(u,f,c):
    last[u] = f
    dist[u] = dist[f] + c
    for v, w in g[u]:
        if v != f:
            dfs(v, u,w)

def road():
    global start, end, d

    dist[1] = 0
    dfs(1, 0)
    start = 1
    for i in range(2, n + 1):
        if dist[i] > dist[start]:
            start = i
    
    dist[start] = 0
    dfs(start, 0)

    end = start
    for i in range(1, n + 1):
        if dist[i] > dist[end]:
            end = i
    d = dist[end]

#第二种求树的直径的方法
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