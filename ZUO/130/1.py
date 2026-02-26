import random
import time
from functools import lru_cache


# =============================
# 暴力方法 O(n * v)
# =============================
def maxSum1(arr):
    n = len(arr)
    max_val = max(arr)

    # dp[i][p] = 以 i 结尾，且当前位置最大允许变成 p 的最大变序和
    dp = [[-1] * (max_val + 1) for _ in range(n)]

    def f1(i, p):
        if p <= 0 or i == -1:
            return 0
        if dp[i][p] != -1:
            return dp[i][p]

        cur = min(arr[i], p)
        next_val = f1(i - 1, cur - 1)
        ans = cur + next_val
        dp[i][p] = ans
        return ans

    ans = 0
    for i in range(n):
        ans = max(ans, f1(i, arr[i]))
    return ans


# =============================
# 正式方法 O(n)
# 单调栈优化
# =============================
def maxSum2(arr):
    n = len(arr)
    stack = []
    dp = [0] * n
    ans = 0

    for i in range(n):
        cur_idx = i
        cur_val = arr[i]

        while cur_val > 0 and stack:
            top_idx = stack[-1]
            top_val = arr[top_idx]

            if top_val >= cur_val:
                stack.pop()
            else:
                idx_diff = cur_idx - top_idx
                val_diff = cur_val - top_val

                if val_diff >= idx_diff:
                    dp[i] += sum_range(cur_val, idx_diff) + dp[top_idx]
                    cur_val = 0
                    break
                else:
                    dp[i] += sum_range(cur_val, idx_diff)
                    cur_val -= idx_diff
                    cur_idx = top_idx
                    stack.pop()

        if cur_val > 0:
            dp[i] += sum_range(cur_val, cur_idx + 1)

        stack.append(i)
        ans = max(ans, dp[i])

    return ans


# =============================
# 等差数列求和
# 从 max 开始往下取 n 项（只取正数部分）
# =============================
def sum_range(max_val, n):
    n = min(max_val, n)
    return ((2 * max_val - n + 1) * n) // 2


# =============================
# 随机数组生成
# =============================
def random_array(n, v):
    return [random.randint(0, v - 1) for _ in range(n)]


# =============================
# 测试代码
# =============================
if __name__ == "__main__":
    print("功能测试开始")
    n = 100
    v = 100
    test_times = 5000

    for _ in range(test_times):
        size = random.randint(1, n)
        arr = random_array(size, v)
        ans1 = maxSum1(arr)
        ans2 = maxSum2(arr)
        if ans1 != ans2:
            print("出错了!", arr, ans1, ans2)
            break
    print("功能测试结束")

    print("性能测试开始")
    n = 100000
    v = 1000000
    arr = random_array(n, v)

    start = time.time()
    maxSum2(arr)
    end = time.time()

    print("数组长度:", n)
    print("运行时间:", round((end - start) * 1000, 2), "毫秒")
    print("性能测试结束")