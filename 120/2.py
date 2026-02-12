#树的重心第二种求解方式
#以某个节点为根时，每颗子树的节点数不超过总节点数的一半，那么这个节点是重心

n = int(input())
g = []
size = []
maxsub = []

def build():
    global n, g, size, maxsub
    g = [[] for _ in range(n+1)]
    size = [0]*(n+1)
    maxsub = [0]*(n+1)
    
def add_edge(u, v):
    g[u].append(v)
    g[v].append(u)
def dfs(u, f):
    global n, g, size, maxsub
    size[u] = 1
    maxsub[u] = 0
    for v in g[u]:
        if v != f:
            dfs(v, u)
            size[u] += size[v]
            maxsub[u] = max(maxsub[u], size[v])
    maxsub[u] = max(maxsub[u], n - size[u])


def get_center():
    global n, g, size, maxsub
    center = [] 
    h = n//2
    for i in range(1, n+1):
        if maxsub[i] <= h:
            center.append(i)
    return center

