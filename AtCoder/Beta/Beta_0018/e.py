import sys
from functools import cache
n,k,b = map(int,sys.stdin.readline().split())
arr = []
for _ in range(n):
    c,s = map(int,sys.stdin.readline().split())
    arr.append([c,s])
arr = [[0,0]] + arr
inf = float('inf')

dp = [[inf]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    if(arr[i][0]<=b):
        dp[i][1] = arr[i][0]

for i in range(1,n+1):
    for j in range(2,k+1):
        for p in range(1,i):
            if arr[p][1]<arr[i][1] and dp[p][j-1]!=inf:
                dp[i][j] = min(dp[i][j],dp[p][j-1]+arr[i][0])

ans = 0
for i in range(1,n+1):
    for j in range(1,k+1):
        if dp[i][j]<=b:
            ans = max(ans,j)
print(ans)
