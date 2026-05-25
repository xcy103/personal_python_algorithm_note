import sys

n,s = map(int,input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.sort()
dp = [-1]*(s+1)
dp[0] = 0
for i in range(n):
    for j in range(s,arr[i][1]-1,-1):
        if dp[j-arr[i][1]]>=0:
            dp[j] = max(dp[j],dp[j-arr[i][1]]+arr[i][0])
print(dp[-1] if dp[-1]>0 else -1)

