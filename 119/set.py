#  三个点，肯定只有两个或者一个最近公共祖先，一个的情况好解释；
#  两个的情况就相当于其中的两个点的公共祖先和另一个点找公共祖先


#  紧急集合
#  一共有n个节点，编号1 ~ n，一定有n-1条边连接形成一颗树
#  从一个点到另一个点的路径上有几条边，就需要耗费几个金币
#  每条查询(a, b, c)表示有三个人分别站在a、b、c点上
#  他们想集合在树上的某个点，并且想花费的金币总数最少
#  一共有m条查询，打印m个答案
#  1 <= n <= 5 * 10^5
#  1 <= m <= 5 * 10^5
#  测试链接 : https://www.luogu.com.cn/problem/P4281

LOG = 0
g = []
deep = []
parent = []

def build(n):
    global g,deep,parent,LOG
    LOG = n.bit_length()
    g = [[] for _ in range(n + 1)]
    deep = [0] * (n + 1)
    parent = [[0]*(LOG) for _ in range(n + 1)]


def add_edge(u, v):
    g[u].append(v)
    g[v].append(u)

def dfs(u, fa):
    parent[u][0] = fa
    deep[u] = deep[fa] + 1
    for p in range(1, LOG):
        parent[u][p] = parent[parent[u][p - 1]][p - 1]
    for v in g[u]:
        if v != fa:
            dfs(v, u)

def lca(a, b):
    if deep[a] < deep[b]:
        a, b = b, a
    
    for p in range(LOG - 1, -1, -1):
        if deep[parent[a][p]] >= deep[b]:
            a = parent[a][p]
    
    if a == b:
        return a

    for p in range(LOG - 1, -1, -1):
        if parent[a][p] != parent[b][p]:
            a = parent[a][p]
            b = parent[b][p]
    return parent[a][0]

def solve(a, b, c):
    h1 = lca(a, b)
    h2 = lca(b, c)
    h3 = lca(c, a)
    
    if h1!=h2:
        high = h1 if deep[h1]<deep[h2] else h2
        low =  h1 if deep[h1]>deep[h2] else h2
    else:
        high = h1
        low = h3
    
    togather = low
    cost = deep[a] + deep[b] + deep[c] - deep[high]*2 - deep[low]

