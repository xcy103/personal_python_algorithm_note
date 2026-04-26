from bisect import bisect_left
class Fenwick:
    def __init__(self, n: int):
        self.f = [0] * n

    def update(self, i: int, val: int) -> None:
        f = self.f
        while i < len(f):
            f[i] = max(f[i], val)
            i += i & -i

    def pre_max(self, i: int) -> int:
        f = self.f
        res = 0
        while i > 0:
            res = max(res, f[i])
            i &= i - 1
        return res


class Solution:
    def maxAlternatingSum(self, nums: list[int], k: int) -> int:
        # 离散化 nums
        sorted_nums = sorted(set(nums))

        n = len(nums)
        f_inc = [0] * n  # f_inc[i] 表示以 nums[i] 结尾且最后两项递增的交替子序列的最大和
        f_dec = [0] * n  # f_dec[i] 表示以 nums[i] 结尾且最后两项递减的交替子序列的最大和

        # 值域树状数组
        m = len(sorted_nums)
        inc = Fenwick(m + 1)  # 维护 f_inc[i] 的最大值
        dec = Fenwick(m + 1)  # 维护 f_dec[i] 的最大值

        for i, x in enumerate(nums):
            if i >= k:
                # 在这个时候才把 f_inc[i-k] 和 f_dec[i-k] 添加到值域树状数组中，从而保证转移来源的下标 <= i-k
                j = nums[i - k]
                inc.update(m - j, f_inc[i - k])  # m-j 可以把后缀变成前缀
                dec.update(j + 1, f_dec[i - k])

            j = bisect_left(sorted_nums, x)
            nums[i] = j  # 注意这里修改了 nums[i]，这样上面的 nums[i-k] 无需二分

            f_inc[i] = dec.pre_max(j) + x          # 计算满足 nums[i'] < x 的 f_dec[i'] 的最大值
            f_dec[i] = inc.pre_max(m - 1 - j) + x  # 计算满足 nums[i'] > x 的 f_inc[i'] 的最大值

        return max(max(f_inc), max(f_dec))  # 枚举子序列以 nums[i] 结尾
