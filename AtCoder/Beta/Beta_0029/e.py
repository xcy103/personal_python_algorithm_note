import sys
from functools import lru_cache
INF = 10**18
n,m = list(map(int,sys.stdin.readline().split()))
g = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    u,v,w = list(map(int,sys.stdin.readline().split()))
    g[u][v] = w
s,k = list(map(int,sys.stdin.readline().split()))
arr = list(map(int,sys.stdin.readline().split()))

#floyd
for t in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            g[i][j] = min(g[i][t]+g[t][j],g[i][j])
ans = INF
#开始dp，

@lru_cache(None)
def f(mask,pre):
    if mask==(1<<k)-1:
        return g[pre][s]
    ans = INF
    for i in range(k):
        if (mask>>i&1)==0:
            ans = min(ans,g[pre][arr[i]]+f(mask^(1<<i),arr[i]))
    return ans
ans = f(0,s)
print(-1 if ans==INF else ans)