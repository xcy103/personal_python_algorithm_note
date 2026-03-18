#  分成k份的最大乘积
#  一个数字n一定要分成k份，得到的乘积尽量大是多少
#  数字n和k，可能非常大，到达10^12规模
#  结果可能更大，所以返回结果对 1000000007 取模
#  来自真实大厂笔试，没有在线测试，对数器验证
import random

MOD = 1000000007

class Solution:

    # 暴力递归（验证用，小数据）
    def maxValue1(self, n, k):
        return self.f1(n, k)

    def f1(self, rest, k):
        if k == 1:
            return rest
        ans = float('-inf')
        for cur in range(1, rest + 1):
            if rest - cur < k - 1:
                break
            ans = max(ans, cur * self.f1(rest - cur, k - 1))
        return ans

    # 贪心 + 快速幂（正式解）
    def maxValue2(self, n, k):
        a = n // k
        b = n % k

        part1 = self.power(a + 1, b)
        part2 = self.power(a, k - b)

        return (part1 * part2) % MOD

    # 快速幂
    def power(self, x, n):
        ans = 1
        x %= MOD
        while n > 0:
            if n & 1:
                ans = ans * x % MOD
            x = x * x % MOD
            n >>= 1
        return ans