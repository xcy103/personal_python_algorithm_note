import sys
from heapq import heappush,heappop
from collections import Counter
n,m,k = map(int,input().split())

g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

c = Counter()
for x in g:
    for y in x:
        if y:
            c[y]+=1
nums = []
for kk,v in c.items():
    nums.append([kk,v])
nums.sort()
op = 0
t = 0

l = len(nums)
for i in range(l-1):
    num,times = nums[i]
    nxt = nums[i+1][0]
    if pow(2,nxt-num)>times:
        while times>1:
            if num+1>=k:
                t+=times//2
            op+=times//2
            times//=2
            num+=1
    else:
        while num<nxt:
            if num+1>=k:
                t+=times//2
            op+=times//2
            times//=2
            num+=1
        nums[i+1][1]+=times

num = nums[-1][0]
times = nums[-1][1]
while times>1:
    if num+1>=k:
        t+=times//2
    num+=1
    op+=times//2
    times//=2
print(op,t)