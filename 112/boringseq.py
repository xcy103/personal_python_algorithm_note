
import sys

MAXN = 100005
diff = [0]*MAXN
sum_tree = [0]*(MAXN<<2)
add_tree = [0]*(MAXN<<2)

def up(i):
    sum_tree[i] = sum_tree[i<<1] + sum_tree[i<<1|1]

def lazy(i,v,n):
    sum_tree[i] += v*n
    add_tree[i] += v

def down(i,ln,rn):
    if add_tree[i]:
        lazy(i << 1, add_tag[i], ln)
        lazy(i << 1 | 1, add_tag[i], rn)
        add_tag[i] = 0

def build(l,r,i):
    add_tree[i] = 0
    if l==r:
        sum_tree[i] = diff[l]
        return 
    mid = (l+r)>>1
    build(l,mid,i<<1)
    build(mid+1,r,1<<1|1)
    up(i)#sum_tree[i] = 0

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

def query(jobl,jobr,jobv,l,r,i):
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

n,m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
diff[0] = arr[0]
for i in range(1,n-1):
    diff[i] = arr[i] - arr[i-1]
out = []
for _ in range(m):
    ops = list(map(int,sys.stdin.readline().split()))
    if len(ops)==5:
        jobl,jobr = ops[1],ops[2]
        k,d = ops[3],ops[4]
        e = k + (r-l)*d
        update(jobl, jobl, k, 1, n, 1)
        if jobl+1<=jobr:
            update(jobl+1, jobr, d, 1, n, 1)
        if jobr<n:
            update(jobr+1, jobr+1, -e, 1, n, 1)
    else:
        p = ops[1]
        out.append(str(query(1,p,1,n,1)))

sys.stdout.write("\n".join(out)+"\n")
