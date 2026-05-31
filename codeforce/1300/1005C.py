import sys
from collections import Counter,defaultdict
n = int(input())
arr = list(map(int,input().split()))

#arr.sort()

pow2 = [1<<i for i in range(1,31)]
c = Counter(arr)
op = 0
for x in arr:
    f = 0
    for n2 in pow2:
        target = n2 - x
        if target in c:
            if target==x and c[target]<2:
                continue
            f = 1
            break
    if not f:
        op+=1
                


print(op)