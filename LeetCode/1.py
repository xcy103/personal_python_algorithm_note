from functools import cache
from functools import lru_cache
class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        s = list(s)
        @cache
        def f(l,r,op):
            if l==r:
                return 1
            if l+1==r:
                if op==0:
                    return 2 if s[l]==s[r] else 1
                return 2 if min(abs(ord(s[l])-ord(s[r])),26-abs(ord(s[l])-ord(s[r])))<=op  else 1
            if s[l]==s[r]:
                return f(l+1,r-1,op)+2
            else:
                p1 = max(f(l+1,r,op),f(l,r-1,op))
                if op>0:
                    if min(abs(ord(s[l])-ord(s[r])),26-abs(ord(s[l])-ord(s[r])))<=op:
                        t =  min(abs(ord(s[l])-ord(s[r])),26-abs(ord(s[l])-ord(s[r])))
                        p1 = max(p1,f(l+1,r-1,op-t)+2)
                return p1
        ans = f(0,n-1,k)
        f.clear_cache()
        return ans
            