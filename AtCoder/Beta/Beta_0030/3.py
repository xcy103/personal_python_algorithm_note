import sys

n,k = list(map(int,sys.stdin.readline().split()))
arr = list(map(int,sys.stdin.readline().split()))
l = 0
op = 0 
while l<n:
    r = l
    while r<n and arr[r]==1:
        r+=1
    if r-l>=k:
        op+=1
    l = max(r,l+1)
print(op)
    