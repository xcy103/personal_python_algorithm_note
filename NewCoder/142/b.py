import sys
from collections import deque
t = int(input())

ans = []
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    q = deque()
    for x in arr[::-1]:
        if not q:
            q.append(x)
        else:
            if x>q[-1]:
                q.append(x)
            else:
                q.appendleft(x)
    ans.append('YES' if list(q)==list(range(1,n+1)) else 'NO')

print('\n'.join(ans))