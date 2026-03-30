import sys

def solve():
    data = sys.stdin.read().split()
    n,m,k = list(map(int,data[:3]))
    arr = list(map(int,data[3:]))

    s = [0]*(n+1)
    for i in range(n):
        s[i+1] = s[i] + arr[i] + m
    vals = []
    for x in s:
        vals.append(x)
        vals.append(x-k)
    uni = sorted(set(vals))
    rank = {v:i+1 for i,v in enumerate(uni)}
    l = len(uni)
    tree = [0]*(l+1)

    def update(i): 
        while i<=l:
            tree[i]+=1
            i+=i&-i
    def query(i):
        ans = 0
        while i:
            ans+=tree[i]
            i&=i-1
        return ans
    res = 0
    for r in range(n+1):
        idx = rank[s[r]-k]
        if r>0:
            res+=query(l) - query(idx-1)
        update(rank[s[r]])
    print(res)

solve()