import sys

n,m = map(int,input().split())

tree = [0]*(n+1)

def add(i):
    while i<=n:
        tree[i]+=1
        i+=i&-i

def query(i):
    ans = 0
    while i:
        ans+=tree[i]
        i&=i-1
    return ans
res = []
for _ in range(m):
    res.append(int(input()))

ans = 0
for x in res[::-1]:
    ans+=query(x-1)
    add(x)
print(ans)