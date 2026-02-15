import sys
import heapq
n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().split()))
k = int(sys.stdin.readline().strip())

l = 0
r = max(arr)+1
t = sum(arr)
while l+1 < r:
    mid = (l+r)//2
    cnt = 0
    for x in arr:
        if x>mid:
            cnt+=(x+k-1)//k
    if cnt > mid:
        l = mid
    else:
        r = mid

print(l)