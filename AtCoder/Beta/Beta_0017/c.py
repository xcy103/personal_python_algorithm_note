import sys
n,q = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
queries = []
for _ in range(q):
    l,r = map(int,sys.stdin.readline().split())
    queries.append((l,r))

nums = [0]*n

sum_tree = [0]*(n+2)

def add(i,v):
    while i<=n:
        sum_tree[i] += v
        i += i&-i

def query(i):
    ans = 0
    while i>0:
        ans += sum_tree[i]
        i -= i&-i
    return ans

def query_sum(l,r):
    ans = query(r)
    if l>=1:
        ans -= query(l-1)
    return ans


for i in range(n-1):
    if arr[i]==arr[i+1]:
        add(i+1,1)


res = []
for l,r in queries:
    res.append(query_sum(l,r-1))

print('\n'.join(map(str,res)))