import sys

n,k = list(map(int,sys.stdin.readline().split()))
cond = []
for _ in range(k):
    cond.append(list(map(int,sys.stdin.readline().split())))

f = list(range(n+1))
def find(x):
    while x!=f[x]:
        f[x] = f[f[x]]
        x = f[x]
    return f[x]

def unite(x,y):
    fx = find(x)
    fy = find(y)
    if fx!=fy:
        f[fx] = fy
        return True
    return False
c = n
for x,y in cond:
    if unite(x,y):
        c-=1
print(pow(26,c,998244353))