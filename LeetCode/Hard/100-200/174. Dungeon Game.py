class Solution:
    def calculateMinimumHP(self, g: List[List[int]]) -> int:
        m,n = len(g),len(g[0])
        #dp = [[[0]*2 for _ in range(n+1)] for _ in range(m+1)]
        @cache
        def f(i,j):
            if not (0<=i<m and 0<=j<n):
                return inf
            if i==m-1 and j==n-1:
                return max(1,-g[i][j]+1)
            h = g[i][j]
            p1 = f(i+1,j)
            p2 = f(i,j+1)
            ans = inf
            if p1!=inf:
                ans = min(max(1,p1-h),ans)
            if p2!=inf:
                ans = min(max(1,p2-h),ans)
            return ans

        return f(0,0)