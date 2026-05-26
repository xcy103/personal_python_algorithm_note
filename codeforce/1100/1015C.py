import sys

n,m = map(int,input().split())
arr = []
s = 0
total = 0
for _ in range(n):
    a,b = map(int,input().split())
    arr.append([a,b,a-b])
    s+=b
    total+=a
if s>m:
    print(-1)
    exit(0)
arr.sort(key = lambda x:-x[2])
if total<=m:
    print(0)
    exit(0)
op = 0
for i in range(n):
    total-=arr[i][2]
    op+=1
    if total<=m:
        break
print(op)
