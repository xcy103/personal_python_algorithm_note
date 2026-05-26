import sys
from collections import Counter 
n,m = map(int,input().split())
arr = list(map(int,input().split()))

c = Counter(arr)


#二分？

def f(x):
    #可以维持的天数
    global m
    tmp = m
    op = 0
    for v in c.values():
        op+=v//x
    return op>=n
l = 0
r = m//n+1
while l+1<r:
    mid = (l+r)//2
    
    if f(mid): l = mid
    else: r = mid
print(l)