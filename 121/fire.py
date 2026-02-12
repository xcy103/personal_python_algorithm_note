
#  消防(递归版)
#  一共n个节点，编号1~n，有n-1条边连接成一棵树，每条边上有非负权值
#  给定一个非负整数s，表示可以在树上选择一条长度不超过s的路径
#  然后在这条路径的点上建立消防站，每个居民可以去往这条路径上的任何消防站
#  目标：哪怕最远的居民走到消防站的距离也要尽量少
#  返回最远居民走到消防站的最短距离
#  测试链接 : https://www.luogu.com.cn/problem/P2491
#  首先求出直径和直径路径
#  然后在直径路径上进行滑动窗口以及单调队列维护最大值
from collections import deque


MAXN = 300001
n = 0
s = 0
g = [[] for _ in range(MAXN)]
dist = [0] * MAXN
last = [0] * MAXN
pred = [0] * MAXN

path = [False] * MAXN
max_dist = [0] * MAXN

start = 0
end = 0
dia = 0

def add_edge(u, v, w):
    g[u].append([v, w])
    g[v].append([u, w])

def dfs(u,v,w):
    last[u] = v
    dist[u] = dist[v] + w
    pred[u] = w
    for v, vw in g[u]:
        if v != v:
            dfs(v, u, vw)

def road():
    global start, end, dia
    
    dfs(1, 0, 0)
    start = 1
    for i in range(2, n + 1):
        if dist[i] > dist[start]:
            start = i
    
    dfs(start, 0, 0)
    end = 1
    for i in range(2, n + 1):
        if dist[i] > dist[end]:
            end = i
    dia = dist[end]

def max_distance_except_diameter(u, f, c):
    ans = c
    for v, w in g[u]:
        if v != f and not path[v]:
            ans = max(ans, max_distance_except_diameter(v, u, c + w))
    return ans

def dis_prep():
    i = end
    while i != 0:
        path[i] = True
        i = last[i]
    i = end
    while i != 0:
        max_dist[i] = max_distance_except_diameter(i, 0, 0)
        i = last[i]

# =========================
# 单调队列 + 滑动窗口
# =========================

def solve():
    suml = 0
    sumr = 0
    ans = 10**18

    q = deque()
    l = end
    r = end

    while l != 0:
        while r!=0 and sumr - suml + pred[r] <= s:
            while q and max_dist[q[-1]] <= max_dist[r]:
                q.pop()
            sumr+=pred[r]
            q.append(r)
            r = last[r]

        ans = min(ans,max(suml,max_dist[q[0]],dia - sumr))

        if q and q[0] == l:
            q.pop(0)
        
        suml+=pred[l]
        l = last[l]

    return ans


