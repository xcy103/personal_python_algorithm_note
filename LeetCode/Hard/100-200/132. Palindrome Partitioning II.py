class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        s = list(s)

        is_pa = [[False]*n for _ in range(n)]

        for i in range(n):
            is_pa[i][i] = True
        for i in range(n-1):
            is_pa[i][i+1] = s[i]==s[i+1]
        
        for i in range(n-3,-1,-1):
            for j in range(i+2,n):
                if s[i]==s[j]:
                    is_pa[i][j] = is_pa[i+1][j-1]
        
        @cache
        def f(i):
            if i==n:
                return 0
            ans = inf
            for j in range(i,n):
                if is_pa[i][j]:
                    ans = min(f(j+1)+1,ans)
            return ans
        return f(0)-1