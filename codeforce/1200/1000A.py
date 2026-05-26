import sys
from collections import Counter
n = int(input())

c = Counter()
for _ in range(n):
    ch = input().strip()
    c[ch]+=1
for _ in range(n):
    ch = input().strip()
    c[ch]-=1

op = 0
for v in c.values():
    if v>0:
        op+=v
print(op)
