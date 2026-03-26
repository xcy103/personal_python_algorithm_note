#
import sys

n,q = map(int,sys.stdin.readline().split())
d = list(map(int,sys.stdin.readline().split()))
d = [0] + d
que = []
for _ in range(q):
    que.append(int(sys.stdin.readline().strip()))

sum_tree = [0]*(n<<2)

def up(i):
    sum_tree[i] = sum_tree[i<<1] + sum_tree[i<<1|1]

def build(l,r,i):
    global sum_tree
    if l==r:
        sum_tree[i] = 1
    else:
        mid = (l+r)>>1
        build(l,mid,i<<1)
        build(mid+1,r,i<<1|1)
        up(i)

def update(jobk,l,r,i):
    if sum_tree[i]<jobk: return
    if(l==r):
        d[l]-=1
        if d[l]==0:
            sum_tree[i]-=1
    else:
        mid = (l+r)>>1
        if sum_tree[i<<1]>=jobk:
            update(jobk,l,mid,i<<1)
        else:
            update(jobk-sum_tree[i<<1],mid+1,r,i<<1|1)
        up(i)
build(1,n,1)
res = []
for x in que:
    update(x,1,n,1)
    res.append(str(sum_tree[1]))

print('\n'.join(res))


        