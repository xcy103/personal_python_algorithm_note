import sys

n = int(sys.stdin.readline().strip())

edges = []
g = [[] for _ in range(n+1)]
for _ in range(n):
    u,v = map(int,sys.stdin.readline().split())
    g[u].append(v)
    g[v].append(u)

size = [0] * (n+1)  
center = 0
best = 0
def dfs(u,f):
    maxsub = 0
    size[u] = 1
    for v in g[u]:
        if v == f:
            continue
        dfs(v,u)
        size[u] += size[v]
        maxsub = max(maxsub, size[v])
    maxsub = max(maxsub, n - size[u])
    if maxsub < best or (maxsub == best and center > u):
        center = u
        best = maxsub
   
