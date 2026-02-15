# 这里学到一个技巧，枚举回文中心
# 不过还是暴力解法，非暴力就是manacher+后缀数组

class Solution:
    def almostPalindromic(self, s: str) -> int:
        n = len(s)
        ans = 0

        def exp(l,r):
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            nonlocal ans
            ans = max(ans,r-l-1)
        
        for i in range(2*n-1):
            l,r = i//2, (i+1)//2
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            exp(l-1,r)
            exp(l,r+1)
            if ans>=n:return n
        return ans