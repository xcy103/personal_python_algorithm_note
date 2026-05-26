import sys

n,m = map(int,input().split())
s = list(map(int,input().split()))

diff = [0]*(n+2)
for _ in range(m):
    l,r,w = map(int,input().split())
    diff[l]+=w
    if r+1<n+2:
        diff[r+1]-=w
op = 0
pre = 0
for i in range(1,n+1):
    pre+=diff[i]
    if pre>s[i-1]:
        op+=1
print(op)