import sys

n,m = map(int,input().split())

if n==2:
    if m==1:
        print(0,0)
        exit(0)
if m==0:
    print(n,n)
    exit(0)
mn = 0
mx = 0
if 2*m>=n:
    mn = 0
else:
    mn = n-2*m

k = 2
while k*(k-1)//2<m:
    k+=1
mx = n-k
print(mn,mx)