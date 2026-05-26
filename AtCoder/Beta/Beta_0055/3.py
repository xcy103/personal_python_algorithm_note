import sys

n = int(input())
w = list(map(int,input().split()))
c = list(map(int,input().split()))
w.sort()
c.sort()
op = 0
l = 0
r = 0
while l<n and r<n:
    if w[l]<=c[r]:
        l+=1
        r+=1
        op+=1
    elif w[l]>c[r]:
        r+=1
print(op)
        