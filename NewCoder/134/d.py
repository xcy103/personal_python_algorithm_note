import sys
from collections import deque

t = int(input())

res = []

def f(nums):
    n = len(nums)
    mn = deque()
    mx = deque()
    l = 0
    r = 0
    op = 0
    while r<n:
        while mn and nums[mn[-1]]>=nums[r]:
            mn.pop()
        mn.append(r)
        while mx and nums[mx[-1]]<=nums[r]:
            mx.pop()
        mx.append(r)

        while mx and mn and nums[mx[0]]-nums[mn[0]]>1:
            l+=1
            while mn and mn[0]<l:
                mn.popleft()
            while mx and mx[0]<l:
                mx.popleft()
        op+=(r-l+1)
        r+=1
    return op
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    op = f(arr)

    res.append(str(op))

print('\n'.join(res))