#  树上点差分模版(递归版)
#  有n个节点形成一棵树，一开始所有点权都是0
#  给定很多操作，每个操作(a,b)表示从a到b路径上所有点的点权增加1
#  所有操作完成后，返回树上的最大点权
#  测试链接 : https://www.luogu.com.cn/problem/P3128

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

# 读入
n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

power = 0
while (1 << power) <= (n >> 1):
    power += 1

deep = [0]*(n+1)
stjump = [[0]*(power+1) for _ in range(n+1)]
num = [0]*(n+1)

# 第一次DFS：预处理深度 + 倍增表
def dfs1(u,f):
    deep[u] = deep[f] + 1
    stjump[u][0] = f
    for p in range(1,power+1):
        stjump[u][p] = stjump[stjump[u][p-1]][p-1]
    for v in graph[u]:
        if v!=f:
            dfs1(v,u)

def lca(a,b):
    if deep[a] < deep[b]:
        a,b = b,a
    for p in range(power,-1,-1):
        if deep[stjump[a][p]] >= deep[b]:
            a = stjump[a][p]
    if a == b:
        return a
    for p in range(power,-1,-1):
        if stjump[a][p] != stjump[b][p]:
            a = stjump[a][p]
            b = stjump[b][p]
    return stjump[a][0]

def dfs2(u,f):
    for v in graph[u]:
        if v!=f:
            dfs2(v,u)
            num[u] += num[v]
dfs1(1,0)

for _ in range(m):
    u,v = map(int, sys.stdin.readline().split())
    L = lca(u,v)
    LF = stjump[l][0]
    num[u] += 1
    num[v] += 1
    num[L] -= 1
    if LF != 0:
        num[LF] -= 1

dfs2(1,0)
print(max(num[1:]))