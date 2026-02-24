import sys
from functools import lru_cache

sys.setrecursionlimit(10**7)

MOD = 376544743

n, m, k = map(int, sys.stdin.readline().split())
start = list(map(int, sys.stdin.readline().split()))
end = list(map(int, sys.stdin.readline().split()))


def special():
    if n%2==0:
        for i in range(m):
            if start[i]==end[i]:
                return 0
    else:
        for i in range(m):
            if start[i]!=end[i]:
                return 0
    return 1

def get_color(s,j):
    return (s>>(j<<1))&3

def set_color(s,j,v):
    return (s&~(3<<(j<<1))) | (v<<(j<<1))

def different(a,b):
    for j in range(m):
        if get_color(a,j)==get_color(b,j):
            return 0
    return 1

def compute():
    start_status = 0
    end_status = 0

    for j in range(m):
        start_status = set_color(start_status, j, start[j])
        end_status = set_color(end_status, j, end[j])

    @lru_cache(None)
    def f(i,j,s):
        if i==n-1:
            return different(s,end_status)
        if j==m:
            return f(i+1,0,s)
        
        ans = 0
        for c in range(k):
            if (j==0 or get_color(s,j-1)!=c) and \
            get_color(s,j)!=c:
                ans = (ans + f(i,j+1,set_color(s,j,c)))%MOD
        return ans

    return f(1,0,start_status)

if k==2:
    print(special())
else:
    print(compute())