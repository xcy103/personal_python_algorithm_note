import sys
from collections import deque
n,k =  map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

q = deque()
dp = [0]*n
q.append(0)
dp[0] = arr[0]

for i in range(1,n):
    while q and q[0]<i-k:
        q.popleft()
    dp[i] = dp[q[0]]+arr[i]
    while q and dp[q[-1]]<=dp[i]: q.pop()
    q.append(i)
print(dp[-1])

