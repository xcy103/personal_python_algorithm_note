import sys

t = int(input())

res = []
for _ in range(t):
    n,m,x = map(int,input().split())
    if x<n or x>m*n:
        res.append([-1])
    
    
