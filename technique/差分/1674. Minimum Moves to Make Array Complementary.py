#就是看那些区间可以+0那些可以+1那些＋2
class Solution:
    def minMoves(self, nums, limit):
        n = len(nums)
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = min(nums[i], nums[n - 1 - i])
            b = max(nums[i], nums[n - 1 - i])

            # 默认 +2
            diff[2] += 2
            diff[2 * limit + 1] -= 2

            # 变成 1 次操作
            diff[a + 1] -= 1
            diff[b + limit + 1] += 1

            # 变成 0 次操作
            diff[a + b] -= 1
            diff[a + b + 1] += 1

        res = float('inf')
        cur = 0

        for s in range(2, 2 * limit + 1):
            cur += diff[s]
            res = min(res, cur)

        return res