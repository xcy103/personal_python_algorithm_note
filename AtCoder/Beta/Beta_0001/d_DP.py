# https://atcoder.jp/contests/awc0001/tasks/awc0001_d

import sys
from functools import lru_cache

# 增加递归深度
sys.setrecursionlimit(2000)

# 读取数据
line1 = sys.stdin.readline().split()
if not line1:
    exit()
n, m, k = map(int, line1)

arr = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    arr.append(row) # [Profit, Cost]

@lru_cache(None)
def f(i, c):
    """
    i: 当前处理到的城市索引
    c: 当前剩余的预算 (M)
    返回从城市 i 开始往后能获得的最大总利润
    """
    # 当前城市的利润
    res = arr[i][0]
    
    max_sub_profit = 0
    # 尝试跳到下一个城市 j，距离不能超过 k
    for j in range(i + 1, min(i + k + 1, n)):
        # 如果钱够付下一个城市的账
        if c >= arr[j][1]:
            # 在所有可能的下一站中选利润最大的
            sub_profit = f(j, c - arr[j][1])
            if sub_profit > max_sub_profit:
                max_sub_profit = sub_profit
                
    return res + max_sub_profit

# 主逻辑
ans = 0
# 挑选任何一个城市作为“第一站”
for i in range(n):
    if m >= arr[i][1]:
        # 初始调用：减去第一站的钱，开始递归
        ans = max(ans, f(i, m - arr[i][1]))

print(ans)