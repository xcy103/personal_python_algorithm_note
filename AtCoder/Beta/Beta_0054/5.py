import sys

n,m = map(int,input().split())

arr = list(map(int,input().split()))

tree = [0]*(n+1)


def update(i):
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
for x in arr:
    res.append(str(x-query(x)))
    update(x)
print('\n'.join(res))