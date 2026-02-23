import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    g = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)

    for _ in range(n-1):
        u, v,w = map(int, input().split())
        g[u].append((v,w))
        g[v].append((u,w))
        degree[v] += 1
        degree[u] += 1
    flow = [0] * (n + 1)
    dp = [0] * (n + 1)

    def dfs1(u,f):
        for v,w in g[u]:
            if v==f:continue
            dfs1(v,u)

        for v,w in g[u]:
            if v==f:continue
            if degree[v]==1:
                flow[u] += w
            else:
                flow[u] += min(flow[v],w)
    
    def dfs2(u,f):
        for v,w in g[u]:
            if v==f:continue
            if degree[v]==1:
                dp[v] = flow[v] + w
            else:
                uflow = flow[u] - min(flow[v],w)
                dp[v] = flow[v] + min(w,uflow)
            dfs2(v,u)
    
    dfs1(1,0)
    dp[1] = flow[1]
    dfs2(1,0)

    print(max(dp))
