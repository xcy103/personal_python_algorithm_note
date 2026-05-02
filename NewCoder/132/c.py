#非常巧，就是统计1的数量
#然后相邻不互质的靠右的改为0
import sys
from math import gcd
t = int(input())

res = []
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    op = 0
    for x in arr:
        if x==1:
            op+=1
    
    for i in range(1,n):
        if arr[i-1]>1 and arr[i]>1 and gcd(arr[i],arr[i-1])==1:
            arr[i] = 0
            op+=1
    res.append(str(op))

print('\n'.join(res))