import sys
from bisect import bisect_left
t = int(input())

res = []

def f(nums):
    pass

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    arr.reverse()

    op = [0]*n
    op[0] = 1
    for i in range(1,n):
        op[i] = min(arr[i],op[i-1])+1
    res.append(str(op[-1]))

print('\n'.join(res))