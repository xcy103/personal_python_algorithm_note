# https://atcoder.jp/contests/awc0001/tasks/awc0001_e

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

mx = deque()
mn = deque()

ans = float('-inf')

l = 0
for r in range(n):
    # 维护最大队列
    while mx and data[mx[-1]] <= data[r]:
        mx.pop()
    mx.append(r)

    # 维护最小队列
    while mn and data[mn[-1]] >= data[r]:
        mn.pop()
    mn.append(r)

    # 如果窗口超过k，缩左边
    if r - l + 1 > k:
        if mx[0] == l:
            mx.popleft()
        if mn[0] == l:
            mn.popleft()
        l += 1

    # 当窗口长度刚好为k
   
    ans = max(ans, data[mx[0]] - data[mn[0]])

print(ans)
