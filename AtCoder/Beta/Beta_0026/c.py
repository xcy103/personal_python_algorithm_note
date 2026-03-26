import sys
from itertools import accumulate
n,t,e = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
x = e//t
pre = list(accumulate(arr))
i = 0
while i<n:
    if pre[i]>x: break
    i+=1
print(i)