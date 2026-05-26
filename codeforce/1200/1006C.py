import sys
from itertools import accumulate
from bisect import bisect_left
n = int(input())
arr = list(map(int,input().split()))
pre = list(accumulate(arr))
suf = [0]*n
suf[-1] = arr[-1]
for i in range(n-2,-1,-1):
    suf[i] = suf[i+1]+arr[i]
suf.reverse()
ans = 0
for i in range(n-1):
    target = pre[i]
    idx = bisect_left(suf,target,0,n-2-i)
    if idx>n-1-i:continue
    if suf[idx]==target:
        ans = pre[i]
print(ans)