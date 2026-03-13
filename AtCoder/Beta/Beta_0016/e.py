#怎么说呢，看答案可以看懂，就是分两步计算
#先算出正的收益，也就是每个经过每个节点的收益，用mask算，这道题数据量不大
#然后要算沿途的花费，先用Floyd算出全员最短路，
#然后用DP算最后的收益，定义状态为dp[经过哪些点][最后停留位置]
#dp[1<<s][s] = 0,这是开始状态
#然后先枚举前一个点，找到合法状态后，开始枚举下一个点
import sys

n,m = map(int,sys.stdin.readline().split())
spots = list(map(int,sys.stdin.readline().split()))
s,t = map(int,sys.stdin.readline().split())
s-=1
t-=1

edges = []
inf = float('inf')
dis = [[inf]*n for _ in range(n)]
g = [[] for _ in range(n)]
for _ in range(m):
    u,v,w = map(int,sys.stdin.readline().split())
    u-=1
    v-=1
    dis[u][v] = w
    dis[v][u] = w

for i in range(n):
    dis[i][i] = 0
#先Floyd处理最近距离
for k in range(n):
    for i in range(n):
        for j in range(n):
            dis[i][j] = min(dis[i][j],dis[i][k]+dis[k][j])

#价值列表
values = [0]*(1<<n)
for mask in range(1<<n):
    for i in range(n):
        if mask>>i&1:
            values[mask]+=spots[i]

dp = [[inf]*n for _ in range(1<<n)]

dp[1<<s][s] = 0

for mask in range(1<<n):
    for i in range(n):
        if dp[mask][i]==inf: continue
        for j in range(n):
            if mask>>j&1: continue

            new_mask = mask|(1<<j)  
            dp[new_mask][j] = min(
                dp[new_mask][j],
                dp[mask][i]+dis[i][j]
            )


ans = -inf
for mask in range(1<<n):
    if mask>>s&1 and mask>>t&1:
        if dp[mask][t] == inf: continue
        ans = max(ans,values[mask]-dp[mask][t])

print(ans)

