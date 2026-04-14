import sys
from functools import lru_cache,cache
@lru_cache(maxsize=None)
t = int(sys.stdin.readline().strip())
arr = []
for _ in range(t):
    arr.append(int(sys.stdin.readline().strip()))
res = []
for y in arr:
    if y<14:
        res.append('-1')
    elif y==14:
        res.append('0')
    else:
        def f(num):
            return 2018*pow(num,4)+5*pow(num,3)+5*pow(num,2)+21*num+14
        l = 0
        r = 100
        sml = 1e-5
        while l+sml<r:
            mid = (l+r)/2
            if(f(mid)>=y): r = mid
            else: l = mid
        res.append(str(round(r, 4)))
print('\n'.join(res))