import sys
x,l,r=map(int,sys.stdin.readline().split())
k=2
while k*k<x:
    res=k*k
    while x%res==0:
        x//=res
    k+=1
i=1
while i*i*x<l:
    i+=1
if i*i*x<=r:
    print(i*i*x)
else:
    print(-1)
