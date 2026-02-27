g = [[5,2,4],[3,0,5],[0,7,2]]
k = 3

m,n = len(g),len(g[0])
MOD = 10**9+7
dp = [[[]*k for _ in range(n)] for _ in range(m)]

dp[0][0][g[0][0]%k] = 1
for i in range(1,m):
    c = g[i][0]%k
    for l in range(k):
        dp[i][0][(l+c)%k] = dp[i-1][0][l]
for i in range(1,n):
    c = g[0][i]%k
    for l in range(k):
        dp[0][i][(l+c)%k] = dp[0][i-1][l]

for i in range(1,m):
    for j in range(1,n):
        c = g[i][0]%k
        for l in range(k):
            dp[i][j][(l+c)%k] = (dp[i-1][j][l] + dp[i][j-1][l])%MOD
print( dp[-1][-1][0])