import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())

# 邻接表
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

size = [0]*(n+1)
sumv = [0]*(n+1)
dp = [0]*(n+1)

def dfs1(u,f):
    size[u] = 1
    sumv[u] = 0
    for v in g[u]:
        if v!=f:
            dfs1(v,u)
            size[u]+=size[v]
            sumv[u]+=sumv[v]+size[v]

def dfs2(u,f):
    for v in g[u]:
        if v==f: continue
        dp[v] = dp[u] + n - 2*size[v]
        dfs2(v,u)

dfs1(1,0)
dp[1] = sumv[1]
dfs2(1,0)
print(max(dp))