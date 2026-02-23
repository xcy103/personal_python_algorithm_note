import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

n, k = map(int, input().split())

g = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int,sys.stdin.readline().split())
    g[u].append(v)
    g[v].append(u)

sumv = [[]*(k+1) for _ in range(n+1)]
dp = [[]*(k+1) for _ in range(n+1)]

values = list(map(int, input().split()))
for i in range(1, n + 1):
    sumv[i][0] = values[i - 1]

def dfs1(u,f):
    for v in g[u]:
        if v==f:continue
        dfs1(v,u)

        for j in range(1,k+1):
            sumv[u][j]+=sumv[v][j-1]
        
def dfs2(u,f):
    for v in g[u]:
        if v==f:continue

        dp[v][0] = sumv[v][0]
        if k>=1:
            dp[v][1] = sumv[v][1] + dp[u][0]
        
        for i in range(2,k+1):
            dp[v][i] = (
                sumv[v][i]
                + dp[u][i-1]
                - sumv[u][i-2]
            )
        
        dfs2(v,u)
    
dfs1(1,0)

for i in range(k+1):
    dp[1][i] = sumv[1][i]

dfs2(1,0)
for i in range(1,n+1):
    print(sum(dp[i]))