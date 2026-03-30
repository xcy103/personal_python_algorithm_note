import sys
from functools import lru_cache
n,k = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
p = list(map(int,sys.stdin.readline().split()))
MOD = 10**9+7

dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][k] = 1

for i in range(n-1,-1,-1):
    for j in range(k-1,-1,-1):
        res = dp[i+1][j]
        if(arr[i]==p[j]):
            res = (res + dp[i+1][j+1])%MOD
        dp[i][j] = res

print(dp[0][0])

            