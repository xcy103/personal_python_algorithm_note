# 同时本题利用了重心的性质:
# 如果树上的边权都是正数，不管边权具体怎么分布，所有节点走到重心的总距离和最小

# 牛群聚集（递归版）
# 树 + 点权(cow) + 边权
# 所有牛汇聚到一个点，使得总距离最小
# 结论：所有牛走向「重心」时，总距离最小

n = int(input())
cow = []
g = []
cowSum = 0
size = []
path = []
best = 0
center = 0

def build():
    global g, size, path, best
    g = [[] for _ in range(n+1)]
    size = [0] * (n+1)
    path = [0] * (n+1)
    best = inf

def add_edge(u, v, w):
    g[u].append((v,w))
    g[v].append((u,w))

def find_center(u, f):
    global center, best
    size[u] = cow[u]
    for v, w in g[u]:
        if v != f:
            find_center(v, u)
            
    maxsub = 0
    for v,_ in g[u]:
        if v != f:
            size[u] += size[v]
            maxsub = max(maxsub, size[v])
    maxsub = max(maxsub, cowSum - size[u])
    if maxsub < best:
        best = maxsub
        center = u

def set_path(u, f):
    for v, w in g[u]:
        if v != f:
            path[v] = path[u] + w
            set_path(v, u)

def compute():
    global cowSum
    cowSum = sum(cow)
    find_center(1, 0)
    path[center] = 0
    set_path(center, 0)
    res = 0
    for i in range(1, n+1):
        res += path[i] * cow[i]
    return res