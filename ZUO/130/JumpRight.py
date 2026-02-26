#  向右跳跃获得最大得分
#  给定长度为n+1的数组arr，下标编号0 ~ n，给定正数a、b
#  一开始在0位置，每次可以选择[a,b]之间的一个整数，作为向右跳跃的距离
#  每来到一个位置i，可以获得arr[i]作为得分，位置一旦大于n就停止
#  返回能获得的最大得分
#  1 <= n <= 2 * 10^5
#  1 <= a <= b <= n
#  -1000 <= arr[i] <= +1000
#  测试链接 : https://www.luogu.com.cn/problem/P1725

import sys

from collections import deque

def solve():
    input = sys.stdin.readline
    n, a, b = map(int, input().split())
    arr = list(map(int, input().split()))
    
    INF = int(1e9)
    dp = [-INF] * (n + 1)
    dp[0] = arr[0]

    q = deque()
    for i in range(1,n+1):
        j = i-a
        if j>=0 and dp[j]!=-INF:
            while q and q[-1][0]<=dp[j]: q.pop()
            q.append(j)
        
        while q and q[0]<=i-b-1: q.popleft()

        if q:
            dp[i] = dp[q[0]] + arr[i]
    return max(dp[max(0, n - b + 1): n + 1])

if __name__ == '__main__':
    print(solve())