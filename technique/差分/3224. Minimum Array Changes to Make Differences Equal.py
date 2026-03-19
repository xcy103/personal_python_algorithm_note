#差分好题。。真他妈难啊
# 核心结论：
# 枚举目标差值 X（0 ~ k），统计把所有对 (p,q) 变成差值 X 的最少操作次数
# 对每一对 (p,q)，设 p <= q：
# x = q - p
# mx = max(q, k - p)
#
# 对 X 的影响：
# 1. X == x           -> 0 次
# 2. X in [0, x-1]    -> 1 次
# 3. X in [x+1, mx]   -> 1 次
# 4. X in [mx+1, k]   -> 2 次
#
# 用差分数组统计每个 X 的总操作次数
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d = [0] * (k + 2)
        for i in range(n // 2):
            p, q = nums[i], nums[n - 1 - i]
            if p > q:  # 保证 p <= q
                p, q = q, p
            x = q - p
            mx = max(q, k - p)
            # [0, x-1] 全部 +1：把 q-p 改成小于 x 的，只需要改 p 或 q 中的一个数
            d[0] += 1
            d[x] -= 1
            # [x+1, mx] 全部 +1：把 q-p 改成大于 x 小于等于 mx 的，也只需要改 p 或 q 中的一个数
            d[x + 1] += 1
            d[mx + 1] -= 1
            # [mx+1, k] 全部 +2：把 q-p 改成大于 mx 的，p 和 q 都需要改
            d[mx + 1] += 2
        return min(accumulate(d))