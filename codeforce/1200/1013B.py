import sys
from collections import Counter,defaultdict

n,x = map(int,input().split())
arr = list(map(int,input().split()))

d = defaultdict(int)
for y in arr:
    d[y]+=1
if max(d.values())>1:
    print(0)
    exit(0)
after = defaultdict(int)
for k in d.keys():
    op = k&x
    after[op]+=1
    if op==k:continue
    if op in d:
        print(1)
        exit(0)
    
if max(after.values())>1:
    print(2)
    exit(0)
print(-1)


