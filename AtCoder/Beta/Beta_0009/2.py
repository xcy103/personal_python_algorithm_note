import sys

n,s,c = map(int,sys.stdin.readline().split())
arr = []
for _ in range(n):
    h,p = map(int,sys.stdin.readline().split())
    arr.append((h,p))

ret = 0
for h,p in arr:
    if s>=h:
        s-=h-p
    else:
        ret+=c
print(ret)