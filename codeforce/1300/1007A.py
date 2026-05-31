import sys

n = int(input())
arr = list(map(int,input().split()))

arr.sort()
l = 0
r = 0
op = 0
while l<n and r<n:
    if arr[l]<=arr[r]:
        l+=1
    else:
        l+=1
        r+=1
        op+=1
print(op)