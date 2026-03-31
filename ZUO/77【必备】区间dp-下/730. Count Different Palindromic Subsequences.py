#  统计不同回文子序列
#  给你一个字符串s，返回s中不同的非空回文子序列个数
#  由于答案可能很大，答案对 1000000007 取模
#  测试链接 : https://leetcode.com/problems/count-different-palindromic-subsequences/
"""
核心思路：按“首尾字符”去重（本题最关键思想）

定义：
dp(l, r) 表示区间 [l, r] 内不同回文子序列的数量

做法：
枚举字符 ch ∈ {'a','b','c','d'}，作为回文的首尾

步骤：
1. 在区间 [l, r] 中找到：
   l = 第一个 ch 出现的位置
   r = 最后一个 ch 出现的位置

2. 分类讨论：

   情况1：不存在 ch
   -> 跳过

   情况2：只出现一次（l == r）
   -> 只形成一个回文："ch"
   -> 贡献：+1

   情况3：出现至少两次（l < r）
   -> 可以形成：
      "ch"              （单字符）
      "chch"            （两端包）
      "ch + 中间回文 + ch"

   -> 中间部分就是 dp(l+1, r-1)

   -> 总贡献：
      2 + dp(l+1, r-1)

最终：
dp(l, r) = sum(每个字符的贡献)

关键点（面试重点）：
1. 不是枚举子序列，而是枚举“回文的首尾字符”
2. 利用最左 + 最右来去重（避免重复统计）
3. 本质是在构造不同回文，而不是数方案

复杂度：
O(4 * n^2) ≈ O(n^2)

注意：
该方法依赖字符集很小（题目限定为 'a' ~ 'd'）
"""

from functools import lru_cache

class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7

        @lru_cache(None)
        def dp(left: int, right: int):
            res = 0

            # 枚举首尾字符
            for ch in 'abcd':
                
                # 找这个字符在区间内的最左和最右
                l = s.find(ch, left, right)
                r = s.rfind(ch, left, right)

                # 情况1：没有
                if l == -1:
                    continue

                # 情况2：只有一个
                if l == r:
                    res += 1

                # 情况3：两个及以上
                else:
                    res += 2                      # "ch", "chch"
                    res += dp(l + 1, r)          # 中间部分

            return res % MOD
        dp.cache_clear()
        return dp(0, len(s))