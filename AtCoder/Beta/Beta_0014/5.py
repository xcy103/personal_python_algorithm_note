import sys

n,q = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
arr = [0] + arr 

sum_tree = [0]*(n<<2)
add_tree = [0]*(n<<2)

def up(i):
    sum_tree[i] = sum_tree[i<<1] + sum_tree[i<<1|1]

def lazy(i,v,n):
    sum_tree[i] += v*n
    add_tree[i] += v

def down(i,ln,rn):
    if add_tree[i]:
        lazy(i<<1,add_tree[i],ln)
        lazy(i<<1|1,add_tree[i],rn)
        add_tree[i] = 0

def build(l,r,i):
    if l==r:
        sum_tree[i] = arr[l]
        return
    mid = (l+r)>>1
    build(l,mid,i<<1)
    build(mid+1,r,i<<1|1)
    up(i)

def update(jobl,jobr,jobv,l,r,i):
    if jobl <= l and r <= jobr:
        lazy(i, jobv, r - l + 1)
        return
    mid = (l + r) >> 1
    down(i, mid - l + 1, r - mid)
    if jobl <= mid:
        update(jobl, jobr, jobv, l, mid, i << 1)
    if jobr > mid:
        update(jobl, jobr, jobv, mid + 1, r, i << 1 | 1)
    up(i)

def query(jobl,jobr,l,r,i):
    if jobl <= l and r <= jobr:
        return sum_tree[i]
    mid = (l + r) >> 1
    down(i, mid - l + 1, r - mid)
    ans = 0
    if jobl <= mid:
        ans += query(jobl, jobr, l, mid, i << 1)
    if jobr > mid:
        ans += query(jobl, jobr, mid + 1, r, i << 1 | 1)
    return ans

build(1,n,1)
quries = []
res = []
for _ in range(q):
    ops = list(map(int,sys.stdin.readline().split()))
    quries.append(ops)

for ops in quries:
    if ops[0]==1:
        update(ops[1],ops[2],ops[3],1,n,1)
    else:
        res.append(str(query(ops[1],ops[2],1,n,1)))

print('\n'.join(res))




