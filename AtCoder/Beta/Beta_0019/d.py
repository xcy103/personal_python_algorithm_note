import sys

n,m,t = map(int,sys.stdin.readline().split())
arr = []
op = 0
for _ in range(n):
    a,b,c = map(int,sys.stdin.readline().split())
    if b>=t:
        op+=a
    else: arr.append([a,c])

arr.sort(key = lambda x:x[1])

dp = [0]*(m+1)
for i in range(len(arr)):
    for j in range(m,arr[i][1]-1,-1):
        dp[j] = max(dp[j],dp[j-arr[i][1]] + arr[i][0])
print(dp[-1] + op)

