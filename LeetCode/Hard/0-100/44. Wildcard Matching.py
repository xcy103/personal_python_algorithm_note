class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        s = list(s)
        p = list(p)

        dp = [[False]*(m+1) for _ in range(n+1)]
        dp[0][0] = True
        for j in range(1,m+1):
            if p[j-1]=='*':
                dp[0][j] = dp[0][j-1]
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if p[j-1]==s[i-1] or p[j-1]=='?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
        return dp[-1][-1]