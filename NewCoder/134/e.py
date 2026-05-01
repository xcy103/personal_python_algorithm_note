import sys
from functools import lru_cache
sys.setrecursionlimit(100000)
t = int(input())

res = []


for _ in range(t):
    n = int(input())
    arr = list(input().strip())
    c1 = arr.count('1')
    # #@lru_cache(None)
    # def f(i,a,b):
    #     if i==n:
    #         return a+b
        
    #     c = arr[i]
    #     s = set()
    #     ans = 0
    #     while (a,b,c) not in s:
    #         ans = max(ans,f(i+1,b,c)+a)
    #         s.add((a,b,c))
    #         a,b,c = a^b,b^c,c^a
    #     return ans
    # ans = f(2,arr[0],arr[1])
    # #f.cache_clear()
    res.append(str(max(c1,n-1) if c1!=0 else 0))

print('\n'.join(res))