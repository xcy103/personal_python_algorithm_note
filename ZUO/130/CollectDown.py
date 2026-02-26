#  向下收集获得最大能量
#  有一个n * m的区域，行和列的编号从1开始
#  每个能量点用(i, j, v)表示，i行j列上有价值为v的能量点
#  一共有k个能量点，并且所有能量点一定在不同的位置
#  一开始可以在第1行的任意位置，然后每一步必须向下移动
#  向下去往哪个格子是一个范围，如果当前在(i, j)位置
#  那么往下可以选择(i+1, j-t)...(i+1, j+t)其中的一个格子
#  到达最后一行时，收集过程停止，返回能收集到的最大能量价值
#  1 <= n、m、k、t <= 4000
#  1 <= v <= 100
#  测试链接 : https://www.luogu.com.cn/problem/P3800

import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m, k, t = map(int, input().split())
    
    dp = [[0]*(m+1) for _ in range(n+1)]

    for _ in range(k):
        r,c,v = map(int, input().split())
        dp[r][c] = v
    
    for i in range(2,n+1):
        q = deque()
        prev = dp[i-1]
        for j in range(1,min(m,t)+1):
            while q and prev[q[-1]]<=prev[j]: q.pop()
            q.append(j)
        
        for j in range(1,m+1):
            nj = j+t
            if j<=m:
                while q and prev[q[-1]]<=prev[nj]: q.pop()
                q.append(nj)
            
            while q and q[0]<j-t:
                q.popleft()
            dp[i][j] += prev[q[0]]
    
    return max(dp[-1])

if __name__ == '__main__':
    print(solve())