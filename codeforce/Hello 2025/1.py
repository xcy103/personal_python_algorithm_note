import sys

def solve():
    t = int(input())

    res = []
    for _ in range(t):
        m,n = map(int,input().split())
        res.append(str(max(n,m)+1))
    print('\n'.join(res))

solve()