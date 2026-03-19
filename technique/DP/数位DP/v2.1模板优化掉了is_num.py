# # 3490. Count Beautiful Numbers
# ## 题目大意
# 给定两个正整数 `l` 和 `r`。
# 如果一个正整数满足：
# - **各位数字的乘积可以被各位数字的和整除**
# 则称这个数为 **Beautiful Number（美丽数字）**。
# 请你返回区间 `[l, r]` 内 **Beautiful Number 的数量**（包含 `l` 和 `r`）。
# 数据范围
# 1 <= l <= r < 10^9
from functools import cache
class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        low = list(map(int, str(l)))
        high = list(map(int, str(r)))
        n = len(high)
        diff_lh = n - len(low)  # 这样写无需给 low 补前导零，也无需 is_num 参数

        @cache
        def dfs(i: int, m: int, s: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1 if s and m % s == 0 else 0

            lo = low[i - diff_lh] if limit_low and i >= diff_lh else 0
            hi = high[i] if limit_high else 9

            res = 0
            if limit_low and i < diff_lh:
                res += dfs(i + 1, 1, 0, True, False)  # 什么也不填
                d = 1  # 下面循环从 1 开始
            else:
                d = lo
            # 枚举填数字 d
            for d in range(d, hi + 1):
                res += dfs(i + 1, m * d, s + d, limit_low and d == lo, limit_high and d == hi)
            return res

        return dfs(0, 1, 0, True, True)