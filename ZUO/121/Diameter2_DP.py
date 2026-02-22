#  树的直径模版(树型dp版逻辑小化简)
#  给定一棵树，边权可能为负，求直径长度
#  测试链接 : https://www.luogu.com.cn/problem/U81904
import sys

input = sys.stdin.readline

n = int(input())

# 普通邻接表
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

dist = [0]*(n+1)
dia = float('-inf')

def dp(u,f):
    global dia
    for v,w in graph[u]:
        if v != f:
            dp(v,u)

    for v,w in graph[u]:
        if v != f:
            dia = max(dia, dist[u] + dist[v] + w)
            dist[u] = max(dist[u], dist[v]+w)

dp(1,0)

print(dia)