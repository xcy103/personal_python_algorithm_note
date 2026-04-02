from functools import cache
def longestPalindrome(word1: str, word2: str) -> int:
        n1,n2 = len(word1),len(word2)
        dp1 = [[0]*n1 for _ in range(n1)]
        dp2 = [[0]*n2 for _ in range(n2)]
        w1 = list(word1)
        w2 = list(word2)
        if not (set(w1)&set(w2)):
            return 0
        for i in range(n1):
            dp1[i][i] = 1
        for i in range(n1-1):
            dp1[i][i+1] = 2 if w1[i]==w1[i+1] else 1
        for i in range(n1-3,-1,-1):
            for j in range(i+2,n1):
                if w1[i]==w1[j]:
                    dp1[i][j]==dp1[i+1][j-1]+2
                else:
                    dp1[i][j] = max(dp1[i+1][j],dp1[i][j-1])

        for i in range(n2):
            dp2[i][i] = 1
        for i in range(n2-1):
            dp2[i][i+1] = 2 if w2[i]==w2[i+1] else 1
        for i in range(n2-3,-1,-1):
            for j in range(i+2,n2):
                if w2[i]==w2[j]:
                    dp2[i][j]==dp2[i+1][j-1]+2
                else:
                    dp2[i][j] = max(dp2[i+1][j],dp2[i][j-1])
        @cache
        def f(l,r):
            if l==n1 and r>=0:
                return dp2[0][r]
            if r==-1 and l<n1:
                return dp1[l][n1-1]
            ans = 0
            if w1[l]==w2[r]:
                ans = f(l+1,r-1)+2
            return max(ans,f(l+1,r),f(l,r-1))
            
        ans = f(0,n2-1)
        f.cache_clear()
        return ans

longestPalindrome("afaaadacb","ca")