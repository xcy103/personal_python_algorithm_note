#这道题比较绕
#我们用记忆化搜索，三个参数,i剩余1的个数,j剩余2的个数,当前这一位我要填什么
#这么看和之前左老师讲的有点像，就是从n这个位置出发
#终止条件也有点难，如果i=0，表示剩余的0没了，
#如果j，也就是剩余1的个数不超过limit，而且k==1，也就是这一位我们填的是1，就是一个合法方案
#同理j==0

from functools import cache
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 1_000_000_007
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int, k: int) -> int:
            if i == 0:
                return 1 if k == 1 and j <= limit else 0
            if j == 0:
                return 1 if k == 0 and i <= limit else 0
            if k == 0:
                return (dfs(i - 1, j, 0) + dfs(i - 1, j, 1) - (dfs(i - limit - 1, j, 1) if i > limit else 0)) % MOD
            else:  # else 可以去掉，这里仅仅是为了代码对齐
                return (dfs(i, j - 1, 0) + dfs(i, j - 1, 1) - (dfs(i, j - limit - 1, 0) if j > limit else 0)) % MOD
        ans = (dfs(zero, one, 0) + dfs(zero, one, 1)) % MOD
        dfs.cache_clear()  # 防止爆内存
        return ans