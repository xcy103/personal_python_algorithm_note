import sys

n,r,t = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

res = []
for i in range(n):
    res.append(min(r,t//arr[i]))

print(*res)