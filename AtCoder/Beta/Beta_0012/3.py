import sys

N,K,M = map(int,sys.stdin.readline().split())
exp = []
beg = []
for _ in range(N):
    h,p = map(int,sys.stdin.readline().split())
    if h:
        exp.append(p)
    else:
        beg.append(p)
op = 0
if len(exp)<M or len(beg)<K-M:
    op = -1
else:
    exp.sort(reverse=True)
    beg.sort(reverse=True)
    op = sum(exp[:M]) + sum(beg[:K-M])

print(op)
