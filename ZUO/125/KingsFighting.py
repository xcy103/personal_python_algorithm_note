import sys
from functools import lru_cache

sys.setrecursionlimit(10**7)

n, kings = map(int, sys.stdin.readline().split())
maxs = 1 << n

def get_bit(s,j):
    if j<0 or j>=n:return 0
    return (s>>j)&1

def set_bit(s,j,v):
    return s&(~(1<<j))|(v<<j)

@lru_cache(None)
def f(i,j,s,leftup,k):
    if i==n:
        return 1 if k==0 else 0
    
    if j==n:
        return f(i+1,0,s,0,k)
    left = 0 if j==0 else get_bit(s,j-1)
    up = get_bit(s,j)
    rightup = get_bit(s,j+1)

    ans = f(i,j+1,set_bit(s,j,0),up,k)
    if k and left==0 and up==0 and rightup==0 and leftup==0:
        ans += f(i,j+1,set_bit(s,j,1),up,k-1)
    
    return ans

print(f(0,0,0,0,kings))