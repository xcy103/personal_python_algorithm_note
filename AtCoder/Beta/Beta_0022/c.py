import sys

n,m,k,t = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
queries = []
for _ in range(k):
    queries.append(list(map(int, sys.stdin.readline().split())))

tree = [0] * (n+1)

def add(i,v):
    while i<=n:
        tree[i] += v
        i += i&-i

def query(i):
    res = 0
    while i>0:
        res += tree[i]
        i -= i&-i
    return res

def query_range(l,r):
    return query(r) - query(l-1)

for x in arr:
    add(x, 1)
res = []
for [l,r] in queries:
    if query_range(l,r)>=t:
        res.append('YES')
    else:
        res.append('NO')

print('\n'.join(res))