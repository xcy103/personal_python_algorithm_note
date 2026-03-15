import sys
from functools import lru_cache

def solve():
    a,b = map(int, sys.stdin.readline().split())

    high = list(map(int,str(b)))
    n = len(high)
    low = list(map(int,str(a).zfill(n)))

    @lru_cache(None)
    def dfs(i,pre,fix,limit_low,limit_high):
        if i==n:
            return 1 if fix else 0
        lo = low[i] if limit_low else 0
        hi = high[i] if limit_high else 9

        ans = 0
        for d in range(lo,hi+1):
            if not fix:
                if d==0:
                    ans+=dfs(
                    i+1,0,False,limit_low and d==lo,limit_high and d==hi
                )
                else:
                    ans+=dfs(
                        i+1,d,True,limit_low and d==lo,limit_high and d==hi
                    )
            else:
                if abs(d - pre) >= 2:
                    ans += dfs(
                        i + 1, d, True,
                        limit_low and d == lo,
                        limit_high and d == hi
                    )
        return ans
    return dfs(0,0,False,True,True)          

if __name__ == '__main__':
    print(solve())