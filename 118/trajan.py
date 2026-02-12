# tarjan 算法解决 LCA 问题
# 测试链接：https://www.luogu.com.cn/problem/P3379
# 算法过程：
# 1）处理所有问题，建好每个节点的问题列表，然后遍历树
# 2）来到当前节点 cur，令 visited[cur] = true，表示当前节点已经访问
# 3）遍历 cur 的所有子树，每棵子树遍历完都和 cur 节点合并成一个集合，
#   集合设置 cur 做头节点
# 4）遍历完所有子树后，处理关于 cur 节点的每一条查询 (cur, x)
# 如果发现 x 已经访问过，cur 和 x 的最近公共祖先 = x 所在集合的头节点
# 如果发现 x 没有访问过，那么当前查询先不处理，
#   等到 x 节点时再处理查询 (x, cur) 得到答案

# 如果节点数为 n，查询数量为 m，
# 整个过程的时间复杂度是 O(n + m)，
# 但是只能做批量离线查询。
g = []
queries = []
vis = []
father = []
ans = []

def find(x):
    if father[x] != x:
        father[x] = find(father[x])
    return father[x]

def tarjan(u,parent):
    vis[u] = True
    for v in g[u]:
        if v == parent:
            continue
        tarjan(v,u)
        father[v] = u
    
    for v,idx in queries[u]:
        if vis[v]:
            ans[idx] = find(v)

def build(n):
    global g,queries,vis,father,ans
    g = [[] for _ in range(n+1)]
    queries = [[] for _ in range(n+1)]
    vis = [False] * (n+1)
    father = [i for i in range(n+1)]

def add_edge(u,v):
    g[u].append(v)
    g[v].append(u)

def add_query(u,v,idx):
    queries[u].append((v,idx))
    queries[v].append((u,idx))
    