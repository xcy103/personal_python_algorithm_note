import sys
from itertools import accumulate
import bisect
n,k,q = map(int, sys.stdin.readline().split())
warehouse = list(map(int, sys.stdin.readline().split()))
queries = [list(map(int, sys.stdin.readline().split())) for _ in range(q)]
pre = [0] + list(accumulate(warehouse))
stops = [0]*n
for i in range(n):
    if i==n-1:
        stops[i] = n
        break
    target = pre[i] + k + 1
    idx = bisect.bisect_left(pre, target)
    if idx==n+1:
        stops[i] = idx-1
    else:
        stops[i] = idx
    
ppre = [0] + list(accumulate(stops))
for l,r in queries:
    print(ppre[r]-ppre[l-1])

