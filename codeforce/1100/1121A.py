import sys
from collections import defaultdict
n,m,k = map(int,sys.stdin.readline().split())

power = list(map(int,sys.stdin.readline().split()))
s = list(map(int,sys.stdin.readline().split()))

nums = list(map(int,sys.stdin.readline().split()))

d = defaultdict(list)
for i in range(n):
    d[s[i]].append((power[i],i))

for _,arr in d.items():
    arr.sort(reverse = True)
op = 0
for x in nums:
    school = s[x-1]
    arr = d[school]
    if arr[0][1]!=x-1:
        op+=1
print(op)