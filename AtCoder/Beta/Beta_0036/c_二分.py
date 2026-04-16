import sys
from functools import lru_cache
n,k = list(map(int,sys.stdin.readline().split()))
arr = list(map(int,sys.stdin.readline().split()))

l = min(arr)-1
r = sum(arr)+1
def f(mid):
    ans = 0
    pre = 0
    for i in range(n):
        if arr[i]>mid:return 10**18
        pre+=arr[i]
        if pre>mid:
            pre = arr[i]
            ans+=1
    return ans+1

while l+1<r:
    mid = (l+r)>>1
    if f(mid)>k+1:l = mid
    else: r = mid
print(r)

import sys
n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

l = max(arr) - 1
r = sum(arr)

def f(mid):
    cnt = 1
    pre = 0
    for x in arr:
        if x > mid:
            return float('inf')  # 关键修复
        
        if pre + x > mid:
            cnt += 1
            pre = x
        else:
            pre += x
    return cnt

while l + 1 < r:
    mid = (l + r) >> 1
    if f(mid) <= k + 1:
        r = mid
    else:
        l = mid

print(r)