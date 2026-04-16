import sys

n,m = list(map(int,sys.stdin.readline().split()))
V = list(map(int,sys.stdin.readline().split()))
arr = []
for _ in range(m):
    d,t = list(map(int,sys.stdin.readline().split()))
    arr.append((d+t-1)//t)
arr.sort()
V.sort()
l = 0
r = 0
op = 0 
while l<n and r<m:
    if V[l]>=arr[r]:
        l+=1
        r+=1
        op+=1
    elif V[l]<arr[r]:
        l+=1
print(op)
