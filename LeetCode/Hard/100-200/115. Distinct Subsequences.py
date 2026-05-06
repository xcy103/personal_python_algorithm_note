class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s),len(t)
        s = list(s)
        t = list(t)
        @cache
        def f(i,j):
            if j==-1:
                return 1
            if i==-1:
                return 0
            
            ans = f(i-1,j)
            if s[i]==t[j]:
                ans+=f(i-1,j-1)
            return ans
        return f(m-1,n-1)