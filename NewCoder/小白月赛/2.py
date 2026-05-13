import sys
from collections import defaultdict
n = int(input())

d = defaultdict(list)

for i in range(n):
    ch,score = input().split()
    d[ch].append((int(score),i+1))
if len(d)<6:
    print(-1)
    exit(0)
q = []
s = 0
for i in range(6):
    arr = d[chr(ord('A')+i)]
    arr.sort()
    if arr[-1][0]<60:
        print(-1)
        exit(0)
    s+=arr[-1][0]
    q.append(arr[-1][1])
if s<70*6:
    print(-1)
    exit(0)
print(*q)