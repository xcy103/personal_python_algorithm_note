# 更快的写法见【Python3 写法二】
from bisect import bisect_left, bisect_right
class Solution:
    def kthRemainingInteger(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        # 记录所有偶数的下标
        even_pos = [i for i, x in enumerate(nums) if x % 2 == 0]
        ans = [0] * len(queries)

        for i, (l, r, k) in enumerate(queries):
            # 计算询问对应的 even_pos 的子数组 even_pos[li:ri]
            li = bisect_left(even_pos, l)
            ri = bisect_right(even_pos, r)

            # 推导过程见 1539 题解
            j = bisect_left(range(ri - li), True, key=lambda j: nums[even_pos[li + j]] // 2 - 1 - j >= k)
            ans[i] = (j + k) * 2

        return ans
