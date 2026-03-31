#  多边形三角剖分的最低得分
#  你有一个凸的 n 边形，其每个顶点都有一个整数值
#  给定一个整数数组values，其中values[i]是第i个顶点的值(顺时针顺序)
#  假设将多边形 剖分 为 n - 2 个三角形
#  对于每个三角形，该三角形的值是顶点标记的乘积
#  三角剖分的分数是进行三角剖分后所有 n - 2 个三角形的值之和
#  返回 多边形进行三角剖分后可以得到的最低分
#  测试链接 : https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution:
    def minScoreTriangulation(self, v: List[int]) -> int:
        
        n = len(v)
        dp = [[0]*n for _ in range(n)]

        for l in range(n-3,-1,-1):
            for r in range(l+2,n):
                dp[l][r] =  inf
                for k in range(l+1,r):
                    dp[l][r] = min(dp[l][r],v[l]*v[k]*v[r]+dp[l][k]+dp[k][r])
                
        return dp[0][n-1]
    

class Solution:
    def minScoreTriangulation(self, v: List[int]) -> int:
        
        n = len(v)
        @cache
        def f(l,r):
            if l==r or l+1==r:
                return 0
            ans = inf
            for k in range(l+1,r):
                ans = min(ans,v[l]*v[r]*v[k]+f(l,k)+f(k,r))
            return ans
        return f(0,n-1)