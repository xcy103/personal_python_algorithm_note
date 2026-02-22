#  树的直径模版(两遍dfs)
#  给定一棵树，边权可能为负，求直径长度
#  测试链接 : https://www.luogu.com.cn/problem/U81904
import sys
input = sys.stdin.readline

n = int(input())

# 普通邻接表（不用链式前向星）
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))


dist = [0]*(n+1)
last = [0]*(n+1)

def dfs(u,f):
    for v,w in graph[u]:
        if v != f:
            dist[v] = dist[u] + w
            last[v] = u
            dfs(v,u)

dfs(1,0)

start = 1
for i in range(2,n+1):
    if dist[i] > dist[start]:
        start = i
dist = [0]*(n+1)
dfs(start, 0)
end = 1
for i in range(2,n+1):
    if dist[i] > dist[end]:
        end = i
dia = dist[end]
print(dia)