import sys
from collections import defaultdict
n = int(input())
arr = list(map(int,input().split()))

S = 0
for x in arr:
    S^=x

d = defaultdict(int)

ans = 0
pre = 0
suf = S^arr[0]
for i in range(1,n-1,1):
    pre^=arr[i-1]
    suf^=arr[i]
    d[pre]+=1
    if suf==S:
        ans+=d[S]
print(ans)

