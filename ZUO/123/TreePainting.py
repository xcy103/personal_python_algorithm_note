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


size = [0] * (n + 1)
dp = [0] * (n + 1)

def dfs1(u,f):
    size[u] = 1
    for v in g[u]:
        if v!=f:
            dfs1(v,u)
            size[u]+=size[v]
    #         dp[u]+=dp[v]
    # dp[u]+=size[u]        

def dfs2(u,f):
    for v in g[u]:
        if v!=f:
            dp[v] = dp[u] - size[v] + n - size[v]
            dfs2(v,u)

dfs1(1,0)
dp[1] = sum(size)
dfs2(1,0)
print(max(dp))