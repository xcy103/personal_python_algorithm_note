import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [0] * N
dp[0] = A[0]

dq = deque()
dq.append(0)  # 存下标，保证 dp 单调递减

for i in range(1, N):
    
    # 移除窗口外的
    while dq and dq[0] < i - K:
        dq.popleft()
    
    dp[i] = dp[dq[0]] + A[i]
    
    # 维护单调递减
    while dq and dp[dq[-1]] <= dp[i]:
        dq.pop()
    
    dq.append(i)

print(dp[N-1])