import sys
from functools import lru_cache
n = int(sys.stdin.readline().strip())
P = list(map(int, sys.stdin.readline().split()))
W = list(map(int, sys.stdin.readline().split()))

#枚举
@lru_cache(None)
def f(i,pre,mask):
    if i==n:
        return 0
    ans = 0
    for j in range(n):
        if (mask>>j&1)==0:
            ans = max(ans,f(i+1,P[j],mask|(1<<j))+abs(P[j]-pre)*W[i-1])
    return ans
ans = 0
for i in range(n):
    ans = max(ans,f(1,P[i],1<<i))
print(ans)