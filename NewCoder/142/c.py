import sys
from collections import deque
t = int(input())

ans = []
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    op = 1
    for x in arr:
        if x%op==0:
            op+=1
    ans.append(str(op-1))
print('\n'.join(ans))
