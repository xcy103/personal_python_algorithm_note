import sys
from heapq import heappush,heappop
n,m = list(map(int,sys.stdin.readline().split()))
l = list(map(int,sys.stdin.readline().split()))
t = list(map(int,sys.stdin.readline().split()))
t.sort(reverse=True)
h = []
for x in l:
    heappush(h,-x)

op = 0
for x in t:
    if h and x>-h[0]:
        print(-1)
        exit(0)
    op+=-heappop(h)-x
print(op)
