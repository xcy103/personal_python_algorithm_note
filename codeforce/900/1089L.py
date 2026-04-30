import sys
from collections import Counter,defaultdict
n,k = map(int,sys.stdin.readline().split())

jobs = list(map(int,sys.stdin.readline().split()))
times = list(map(int,sys.stdin.readline().split()))

d = defaultdict(list)
for i in range(n):
    d[jobs[i]].append(times[i])

if len(d)==k:
    print(0)
    exit(0)

res = []
for _,arr in d.items():
    if len(arr)>1:
        tmp = sorted(arr)
        res.extend(tmp[:-1])
res.sort()
print(sum(res[:k-len(d)]))