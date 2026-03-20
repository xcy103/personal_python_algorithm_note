import sys
from functools import lru_cache
n,m = map(int,sys.stdin.readline().split())

inf = float('inf')
dis = [[inf]*(n) for _ in range(n)]
for i in range(n):
    dis[i][i] = 0
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    dis[a-1][b-1] = min(dis[a-1][b-1], c)
    dis[b-1][a-1] = min(dis[b-1][a-1], c)

#floyd
for k in range(n):
    for i in range(n):
        for j in range(n):
            dis[i][j] = min(dis[i][j],dis[i][k]+dis[k][j])
for i in range(n):
    if dis[0][i] == inf:
        print(-1)
        exit()
@lru_cache(None)
def f(mask,pre):
    if mask==(1<<n)-1:
        return dis[pre][0]
    ans = inf
    for i in range(1,n):
        if (mask>>i&1)==0:
            ans = min(ans,dis[pre][i]+f(mask^(1<<i),i))
    return ans
ans = f(1,0)
print(-1 if ans==inf else ans)
