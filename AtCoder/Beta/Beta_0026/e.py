import sys
from collections import deque
n,k = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

inf = 10**10
def f(t):
    qmx = deque()
    qmn = deque()
    l = 0
    r = 0
    ans = 0
    while r<n:
        while qmx and arr[qmx[-1]]<=arr[r]:
            qmx.pop()
        while qmn and arr[qmn[-1]]>=arr[r]:
            qmn.pop()
        qmx.append(r)
        qmn.append(r)
        while qmn and qmx and arr[qmx[0]] - arr[qmn[0]]>t:
            if qmx[0]==l:
                qmx.popleft()
            if qmn[0]==l:
                qmn.popleft()
            l+=1
        ans+=(r-l+1)
        r+=1
    return ans
print(f(k)-f(k-1))