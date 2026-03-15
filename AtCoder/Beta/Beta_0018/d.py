import sys
n,k = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
dp = [0]*(k+1)
for i in range(n):
    for x in range(k,arr[i]-1,-1):
        dp[x] = max(dp[x],dp[x-arr[i]]+arr[i])

print(dp[k])