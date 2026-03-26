#扫描线，开始结束分离
import sys
from heapq import heappop,heappush
n,k = map(int,sys.stdin.readline().split())
cur = 0
h = []
for _ in range(n):
    s,e = map(int,sys.stdin.readline().split())
    heappush(h,(s,1))
    heappush(h,(e+1,-1))
t = 0
pre = -1
res = 0
while h:
    l,v = heappop(h)
    if v==1:
        t+=1
        if t==k:
            pre = l
    else:
        t-=1
        if t==k-1:
            res+=l-pre-1
print(res)