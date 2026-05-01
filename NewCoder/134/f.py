import sys
from functools import lru_cache
sys.setrecursionlimit(100000)
t = int(input())

mod = 998244353
res = []


for _ in range(t):
    n = int(input())
    s = list(input().split()[0])
    
    @lru_cache(None)
    def f(i):
        if i==n:
            return 0
        ans = 0
        for j in range(i+1,n+1):
            l = i
            r = j-1
            tag = 1
            while l<r:
                if s[l]!=s[r]:
                    tag = 0
                    break
                l+=1
                r-=1
            if tag:
                ans = (ans + f(j)+(j-i)**2)%mod
        return ans
    op = f(0)
    f.cache_clear()
    res.append(str(op%mod))

print('\n'.join(res))