import sys

n = int(sys.stdin.readline().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
res = []
def f(x,y):
    ans = 0
    tx = x
    while tx>0:
        ans = max(tx^y,ans)
        tx>>=1
    ty = y
    while ty>0:
        ans = max(ans,ty^x)
        ty>>=1
    return ans
for a,b in arr:
    res.append(str(f(a,b)))

print('\n'.join(res))
