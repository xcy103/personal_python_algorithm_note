import sys
from collections import deque
t = int(input())

ans = []
for _ in range(t):
    n = int(input())
    s = list(input().split()[0])

    q = deque()
    l = 0
    for i,ch in enumerate(s):
        if ch=='!':
            l = 1-l
        elif ch=='-':
            if q:
                if l==0:
                    q.pop()
                else:
                    q.popleft()
        else:
            if l==0:
                q.append(ch)
            else:
                q.appendleft(ch)
    res = ""
    if q:
        res = ''.join(q)
    ans.append(res if res else 'Empty')

print('\n'.join(ans))