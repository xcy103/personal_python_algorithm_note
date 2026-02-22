#  所有直径的公共部分(递归版)
#  给定一棵树，边权都为正
#  打印直径长度、所有直径的公共部分有几条边
#  测试链接 : https://www.luogu.com.cn/problem/P3304
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
last = [0]*(n+1)
diaPath = [False]*(n+1)

start = 0
end = 0
dia = 0
common = 0

def dfs(u, f):
    for v, w in graph[u]:
        if v != f:
            dist[v] = dist[u] + w
            last[v] = u
            dfs(v, u)

def road():
    global start, end, dia,dist
    dfs(1, 0)
    start = 1
    for i in range(2, n + 1):
        if dist[i] > dist[start]:
            start = i
    dist = [0]*(n+1)
    dfs(start, 0)
    end = 1
    for i in range(2, n + 1):
        if dist[i] > dist[end]:
            end = i
    dia = dist[end]

def maxDistanceExceptDiameter(u,f):
    ans = 0
    for v, w in graph[u]:
        if v != f:
            if diaPath[v] == False:
                ans + maxDistanceExceptDiameter(v, u) + w
    return ans

def compute():
    global common
    road()
    cur = end
    while cur != start:
        diaPath[cur] = True
        cur = last[cur]
    
    l = start
    r = end

    i = last[end]
    while i!=start:
        maxDist = maxDistanceExceptDiameter(i,0)
        if maxDist == dia - dist[i]:
            r = i
        if maxDist == dist[i] and l==start:
            l = i
            break
        i = last[i]
    
    if l==r:
        common = 0
    else:
        common = 1
        i = last[r]
        while i != l:
            common += 1
            i = last[i]

compute()

print(dia)
print(common)