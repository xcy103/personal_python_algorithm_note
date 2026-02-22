
#  造公园
#  一共n个节点，编号1~n，有m条边连接，边权都是1
#  所有节点可能形成多个连通区，每个连通区保证是树结构
#  有两种类型的操作
#  操作 1 x   : 返回x到离它最远的点的距离
#  操作 2 x y : 如果x和y已经连通，那么忽略
#               如果不连通，那么执行连通操作，把x和y各自的区域连通起来
#               并且要保证连通成的大区域的直径长度最小
#  测试链接 : https://www.luogu.com.cn/problem/P2195
import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

# 读入
n, m, q = map(int, input().split())

graph = [[] for _ in range(n + 1)]
father = list(range(n + 1))
dist = [0]*(n + 1)
diameter = [0]*(n+1)

def find(x):
    while x != father[x]:
        father[x] = father[father[x]]
        x = father[x]
    return x

# 加边
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    fu = find(u)
    fv = find(v)
    if fu != fv:
        father[fu] = fv

def dp(u,f):
    for v in graph[u]:
        if v!=f:
            dp(v,u)
    for v in graph[u]:
        if v!=f:
            diameter[u] = max(
                diameter[u],
                diameter[v],
                dist[u] + dist[v] + 1
            )
            dist[u] = max(dist[u], dist[v] + 1)

for i in range(1, n + 1): 
    if find(i)==i:
        dp(i,0)

out = []
for _ in range(q):
    tmp = input().split()
    op = int(tmp[0])

    if op==1:
        x = int(tmp[1])
        x = find(x)
        out.append(str(diameter[x]))
    else:
        fx = find(int(tmp[1]))
        fy = find(int(tmp[2]))
        if fx!=fy:
            father[fx] = fy
            diameter[fy] = max(
                (diameter[fy]+1)//2+(diameter[fx]+1)//2+1,
                diameter[fx], diameter[fy]
            )

print('\n'.join(out))