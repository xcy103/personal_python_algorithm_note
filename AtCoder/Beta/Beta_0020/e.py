import sys
n,m = map(int,sys.stdin.readline().split())
w = list(map(int,sys.stdin.readline().split()))
c = list(map(int,sys.stdin.readline().split()))
c = [0] + c
t = len(c)
max_tree = [0]*(t<<2)

def up(i):
    max_tree[i] = max(max_tree[i<<1],max_tree[i<<1|1])

def build(l,r,i):
    if l==r:
        max_tree[i] = c[l]
        return
    mid = (l+r)>>1
    build(l,mid,i<<1)
    build(mid+1,r,i<<1|1)
    up(i)

def update(jobi,l,r,i):
    if l==r:
        max_tree[i] = 0
        return
    mid = (l+r)>>1
    if jobi<=mid :
        update(jobi,l,mid,i<<1)
    else:
        update(jobi,mid+1,r,i<<1|1)
    up(i)
def query(jobv,l,r,i):
    if max_tree[i]<jobv:
        return False
    if l==r:
        update(l,1,m,1)
        return True
    mid = (l+r)>>1
    ans = False
    if max_tree[i<<1]>=jobv:
        ans = query(jobv,l,mid,i<<1)
    if not ans and max_tree[i<<1|1]>=jobv:
        ans = query(jobv,mid+1,r,i<<1|1)
    return ans
build(1,m,1)
op = 0
for x in w:
    if query(x,1,m,1):
        op+=1
print(op)