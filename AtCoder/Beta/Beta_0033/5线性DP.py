import sys
from collections import deque
n,k = list(map(int, sys.stdin.readline().split()))
A = [0]+list(map(int, sys.stdin.readline().split()))

dp = [0]*(n+1)
dp[1] = A[1]
q = deque([1])

for i in range(2,n+1):
    #首先下标出队
    while q and q[0]<i-k:
        q.popleft()
    #转移
    dp[i] = dp[q[0]]+A[i]
    #维护单调递减,从左往右
    while q and dp[q[-1]]>=dp[i]:
        q.pop()
    q.append(i)

print(dp[n])