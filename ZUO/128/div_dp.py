# 核心思维：寻找“切割点”总分的构成：假设我们将珠子分成 $k$ 个区间（背包）。
# 第 1 个包的范围是 $[0, i_1]$，价格为 $w[0] + w[i_1]$。
# 第 2 个包的范围是 $[i_1+1, i_2]$，价格为 $w[i_1+1] + w[i_2]$。...
# 第 $k$ 个包的范围是 $[i_{k-1}+1, n-1]$，价格为 $w[i_{k-1}+1] + w[n-1]$。
# 抵消与合并：当我们把这 $k$ 个价格加起来时，你会发现：
# 首尾不变：$w[0]$ 和 $w[n-1]$ 永远会被计入总分，且只计入一次。
# 切割点决定分值：每个切割处 $i$ 都会产生一对相邻珠子的重量和：$w[i] + w[i+1]$。
# 结论：要将 $n$ 个珠子分成 $k$ 个包，本质上是在 $n-1$ 个相邻空隙中
# 选择 $k-1$ 个位置进行切割。


import sys

def solve():
    # 快速读入
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    arr = [0] * (n + 1)
    for i in range(1, n + 1):
        arr[i] = int(input_data[i])

    # --- 1. 求最大平均值 ---
    def check_avg(x):
        # dp[i][0]: 选了 i 号位置，后续的最大累加和
        # dp[i][1]: 没选 i 号位置（那么 i+1 必须选），后续的最大累加和
        dp0, dp1 = 0.0, 0.0
        for i in range(n, 0, -1):
            val = arr[i] - x
            new_dp0 = max(val + dp0, dp1)
            new_dp1 = val + dp0
            dp0, dp1 = new_dp0, new_dp1
        return dp0 >= 0

    l, r = float(min(arr[1:])), float(max(arr[1:]))
    for _ in range(60): # 二分60次保证精度
        mid = (l + r) / 2
        if check_avg(mid):
            l = mid
        else:
            r = mid
    print(f"{l:.3f}")

    # --- 2. 求最大中位数 ---
    def check_median(x):
        # 类似逻辑，val 为 1 (>=x) 或 -1 (<x)
        dp0, dp1 = 0, 0
        for i in range(n, 0, -1):
            val = 1 if arr[i] >= x else -1
            new_dp0 = max(val + dp0, dp1)
            new_dp1 = val + dp0
            dp0, dp1 = new_dp0, new_dp1
        return dp0 > 0

    sorted_arr = sorted(arr[1:])
    low, high = 0, n - 1
    ans_median = sorted_arr[0]
    while low <= high:
        mid_idx = (low + high) // 2
        if check_median(sorted_arr[mid_idx]):
            ans_median = sorted_arr[mid_idx]
            low = mid_idx + 1
        else:
            high = mid_idx - 1
    print(ans_median)

if __name__ == "__main__":
    solve()