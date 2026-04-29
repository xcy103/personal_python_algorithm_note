import sys

from collections import Counter

arr = list(map(int,sys.stdin.readline().split()))
c = Counter(arr)

res = 0
for k,v in c.items():
    if v%2==1:
        res^=k
print(res)
