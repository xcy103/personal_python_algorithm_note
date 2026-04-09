# 手写 min 更快
min = lambda a, b: b if b < a else a
inf = 10**18
class Solution:
    def minArraySum(self, nums, k: int) -> int:
        min_f = [inf] * k
        min_f[0] = 0  # s[0] = 0，对应的 f[0] = 0
        f = s = 0
        for x in nums:
            s = (s + x) % k
            # 不删除 x，那么转移来源为 f + x
            # 删除以 x 结尾的子数组，问题变成剩余前缀的最小和
            # 其中剩余前缀的元素和模 k 等于 s，对应的 f 值的最小值记录在 min_f[s] 中
            f = min(f + x, min_f[s])
            # 维护前缀和 s 对应的最小和，由于上面计算了 min，这里无需再计算 min
            min_f[s] = f
        return f