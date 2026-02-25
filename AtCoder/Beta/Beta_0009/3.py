import sys

n,t,k = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

d = min(arr)-1
x = d+t+k
op = 0
for h in arr:
    if h<=x:
        op+=1
print(op)