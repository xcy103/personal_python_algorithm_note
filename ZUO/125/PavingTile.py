import sys
from functools import lru_cache

sys.setrecursionlimit(10**7)

def solve(n,m):
    @lru_cache(None)
    def f(i,j,s):
        if i==n:
            return 1
        if j==m:
            return f(i+1,0,s)
        if s>>j&1:
            return f(i,j+1,s&~(1<<j))
        
        ans = 0
        if i+1<n:
            ans+=f(i,j+1,s|(1<<j))
        if j+1<m and ((s>>(j+1))&1)==0:
            ans+=f(i,j+2,s)
        
        return ans
    return f(0,0,0)

for line in sys.stdin:
    n,m = map(int,line.split())
    if n==0 and m==0:break
    print(solve(n,m))