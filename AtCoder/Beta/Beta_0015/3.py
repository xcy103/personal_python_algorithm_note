import sys
from collections import defaultdict,Counter
n = int(sys.stdin.readline().strip())
arr = []
for _ in range(n):
    s,t = map(int,sys.stdin.readline().split())
    arr.append([s,t])

d = defaultdict(list)
for s,t in arr:
    d[s].append(t)
op = 0
for sports in d.values():
    l = len(sports)
    op+=l*(l-1)//2
    c = Counter(sports)
    for v in c.values():
        if v>1:
            op-=v*(v-1)//2
print(op)