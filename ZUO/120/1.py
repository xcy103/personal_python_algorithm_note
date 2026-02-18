#第一种求重心的方法，dfs求出以每个节点最为根节点的最大的子树大小
#
from cmath import inf


n = int(input())
g = []
size = []
center = 0
best = 0


def build():
    global n, g, size, center, best
    g = [[] for _ in range(n+1)]
    size = [0] * (n+1)
    center = 0
    best = inf
    
def add_edge(u, v):
    g[u].append(v)
    g[v].append(u)    

def dfs(u, f):
    global center, best
    size[u] = 1
    max_part = 0
    for v in g[u]:
        if v != f:
            dfs(v, u)
            size[u] += size[v]
            max_part = max(max_part, size[v])
    max_part = max(max_part, n - size[u])
    #找出最小编号的重心
    if max_part < best or (max_part == best and u < center):
        best = max_part
        center = u