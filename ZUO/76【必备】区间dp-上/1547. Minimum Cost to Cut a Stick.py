#  切棍子的最小成本
#  有一根长度为n个单位的木棍，棍上从0到n标记了若干位置
#  给你一个整数数组cuts，其中cuts[i]表示你需要将棍子切开的位置
#  你可以按顺序完成切割，也可以根据需要更改切割的顺序
#  每次切割的成本都是当前要切割的棍子的长度，切棍子的总成本是历次切割成本的总和
#  对棍子进行切割将会把一根木棍分成两根较小的木棍
#  这两根木棍的长度和就是切割前木棍的长度
#  返回切棍子的最小总成本
#  测试链接 : https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
# 这道题难想的是如果计算出切分一下的代价
# 我么可以左添加一个0，右添加一个n，切一次就可以用r+1-(l-1)来计算代价了


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        t = len(cuts)
        c = [0]+cuts+[n]
        @cache
        def f(l,r):
            if l>r:
                return 0
            if l==r:
                return c[r+1] - c[l-1]
            ans = inf
            for k in range(l,r+1):
                ans = min(ans,f(l,k-1)+f(k+1,r)+c[r+1]-c[l-1])
            return ans
        return f(1,t)


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        t = len(cuts)
        c = [0]+cuts+[n]
        dp = [[0]*(t+2) for _ in range(t+2)]
        for i in range(1,t+1):
            dp[i][i] = c[i+1]-c[i-1]
        
        for l in range(t-1,-1,-1):
            for r in range(l+1,t+1):
                tmp = inf
                for k in range(l,r+1):
                    tmp = min(tmp,dp[l][k - 1] + dp[k + 1][r])
                dp[l][r] = c[r+1]-c[l-1]+tmp
        return dp[1][t]
        
        