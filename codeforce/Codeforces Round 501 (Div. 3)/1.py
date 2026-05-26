import sys

n,m = map(int,input().split())

p = [1]*(m+1)
p[0] = 0
for _ in range(n):
    a,b = map(int,input().split())
    for l in range(a,b+1):
        p[l]-=1
res = []

for i in range(1,m+1):
    if p[i]>0:
        res.append(i)
print(len(res))
if res:
    print(*res)