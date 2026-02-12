#  巡逻
#  一共n个节点，编号1~n，结构是一棵树，每条边都是双向的
#  警察局在1号点，警车每天从1号点出发，一定要走过树上所有的边，最后回到1号点
#  现在为了减少经过边的数量，你可以新建k条边，把树上任意两点直接相连
#  并且每天警车必须经过新建的道路正好一次
#  计算出最佳的新建道路的方案，返回巡逻走边数量的最小值
#  测试链接 : https://www.luogu.com.cn/problem/P3629
#  1 <= n <= 10^5
#  1 <= k <= 2
#  k=1时，就是再直径两端之间加一条边
#  k==2 时，先找出直径，然后把直径的边权改为-1，在这个条件下再算直径

MAXN = 100001

n = 0
k = 0

g = [[] for _ in range(MAXN)]
dist = [0] * MAXN
last = [0] * MAXN
path = [False] * MAXN

start = 0
end = 0
d1 = 0
d2 = 0

def add_edge(u,v):
    g[u].append(v)
    g[v].append(u)

def dfs(u,f,c):
    last[u] = f
    dist[u] = dist[f] + c
    for v in g[u]:
        if v != f:
            dfs(v, u, 1)

def road():
    global start, end, d1

    
    dfs(1, 0, 0)
    start = 1
    for i in range(2, n + 1):
        if dist[i] > dist[start]:
            start = i
    
    dfs(start, 0, 0)
    end = 1
    for i in range(1, n + 1):
        if dist[i] > dist[end]:
            end = i
    d1 = dist[end]

def dp(u,f):

    for v in g[u]:
        if v !=f:
            dp(v, u)
    
    for v in g[u]:
        if v!=f:
            w = -1 if path[v] and path[u] else 1
            d2 = max(d2, dist[u] + dist[v] + w)
            dist[u] = max(dist[u], dist[v] + w)

def solve():
    road()
    if k==1:
        print(2*(n-1) - d1 + 1)
    else:
        i = end
        while i != 0:
            path[i] = True
            i = last[i]
        dist = [0] * MAXN
        dp(1,0)
        print(2*(n-1) - d1 - d2 + 2)