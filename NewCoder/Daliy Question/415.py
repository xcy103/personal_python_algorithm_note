import sys
from functools import lru_cache
n = int(sys.stdin.readline().strip())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = list(map(int,sys.stdin.readline().split()))
    g[a].append(b)
mod = 10**9+7
#选1为根节点
#树形DP吗，从子节点开始
#@lru_cache(None)
def dfs(u,pre):
    if len(g[u])==0:
        return 1
    ans = 1
    if pre==0:
        for v in g[u]:
            ans = ans*dfs(v,1)%mod
    else:
        for v in g[u]:
            ans = ans*(dfs(v,1)+dfs(v,0))%mod
    return ans

print(dfs(1,0)+dfs(1,1))
    
