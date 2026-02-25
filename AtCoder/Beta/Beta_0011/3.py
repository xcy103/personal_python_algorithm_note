import sys

n,k = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

seen = set()
for i in range(65):
    if k>>i&1:
        seen.add(i)

op = 0
ans = 0
for x in arr:
    f = 1
    for i in range(65):
        if x>>i&1 and i not in seen:
            f = 0
    if f:
        op+=1
        ans|=x
print(op if op>0 and ans==k else -1)
            