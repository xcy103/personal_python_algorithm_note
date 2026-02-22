#  运输计划
#  有n个节点，给定n-1条边使其连接成一棵树，每条边有正数边权
#  给定很多运输计划，每个运输计划(a,b)表示从a去往b
#  每个运输计划的代价就是沿途边权和，运输计划之间完全互不干扰
#  你只能选择一条边，将其边权变成0
#  你的目的是让所有运输计划代价的最大值尽量小
#  返回所有运输计划代价的最大值最小能是多少
#  测试链接 : https://www.luogu.com.cn/problem/P2680

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# 读入
n, m = map(int, input().split())

g = [[] for i in range(n+1)]

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

query = [[] for _ in range(n+1)]
quesu = [0]*(n+1)
quesv = [0]*(n+1)

for i in range(1, m + 1):
    u, v = map(int, input().split())
    quesu[i] = u
    quesv[i] = v
    query[u].append((v, i))
    query[v].append((u, i))

vis = [False]*(n+1)
unionfind = list(range(n+1))
distance = [0]*(n+1)
lca = [0]*(m+1)
cost = [0]*(m+1)
maxCost = 0

def find(x):
    while x != unionfind[x]:
        unionfind[x] = unionfind[unionfind[x]]
        x = unionfind[x]
    return x

def trajan(u,f,w):
    global maxCost
    vis[u] = True
    distance[u] = distance[f] + w
    for v, weight in graph[u]:
        if not vis[v]:
            trajan(v,u,weight)
    
    for v, idx in query[u]:
        if vis[v]:
            anc = find(v)
            lca[idx] = anc
            cost[idx] = distance[u] + distance[v] - 2 * distance[anc]
            maxCost = max(maxCost, cost[idx])
    unionfind[u] = f


num = [0]*(n+1)
atLeast = 0
beyond = 0

def dfs(u,f,w):
    global atLeast, beyond
    for v, weight in graph[u]:
        if v != f:
            if dfs(v, u, weight):
                return True
    
    for v,weight in graph[u]:
        if v!=f:
            num[u]+=num[v]
    return num[u]>=beyond and w>=atLeast
        

def check(limit):
    global atLeast, beyond
    atLeast = maxCost - limit
    beyond = 0
    num = [0]*(n+1)
    for i in range(1,m+1):
        if cost[i]>limit:
            num[quesu[i]] += 1
            num[quesv[i]] += 1
            num[lca[i]] -= 2
            beyond += 1
    if beyond==0:
        return True
    
    return dfs(1,0,0)

trajan(1,0,0)

left,right = 0,maxCost
ans = 0
while left<=right:
    mid = (left+right)//2
    if check(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1