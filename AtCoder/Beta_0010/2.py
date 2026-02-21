import sys

n,k,q = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
queries = []
for _ in range(q):
    queries.append(list(map(int,sys.stdin.readline().split())))
arr = [0] + arr
father = list(range(n+1))

def find(x):
    if father[x]!=x:
        father[x] = find(father[x])
    return father[x]

def union(x,y):
    fx = find(x)
    fy = find(y)
    if fx!=fy:
        father[fx] = fy
for i in range(1,n):
    if abs(arr[i+1]-arr[i])<=k:
        union(i,i+1)

results = []
for l,r in queries:
    if find(l)==find(r):
        results.append("Yes")
    else:
        results.append("No") 
print("\n".join(results))