class Solution:
    def minimumIncrements(self, nums: List[int], target: List[int]) -> int:
        # 预处理 target 的所有子集的 LCM
        m = len(target)
        lcms = [1] * (1 << m)
        for i, t in enumerate(target):
            bit = 1 << i
            for mask in range(bit):
                lcms[bit | mask] = lcm(t, lcms[mask])

        @cache
        def dfs(i: int, j: int) -> int:
            if j == 0:
                return 0
            if i < 0:  # 不能有剩余元素
                return inf
            # 不修改 nums[i]
            res = dfs(i - 1, j)
            # 枚举 j 的所有非空子集 sub，把 nums[i] 改成 lcms[sub] 的倍数
            sub = j
            while sub:
                l = lcms[sub]
                res = min(res, dfs(i - 1, j ^ sub) + (l - nums[i] % l) % l)
                sub = (sub - 1) & j
            return res
        return dfs(len(nums) - 1, (1 << m) - 1)
