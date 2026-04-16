import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

#首先维护区间最小值，用线段树
min_tree = [0]*(n<<2)

def up(i):
    min_tree[i] = min(min_tree[i<<1],min_tree[i<<1|1])

def build(l,r,i):
    if l==r:
        min_tree[i] = arr[l]
        return
    mid = (l+r)//2
    build(l,mid,i<<1)
    build(mid+1,r,i<<1|1)
    up(i)

def query(jobl,jobr,l,r,i):
    if jobl<=l and jobr>=r:
        return min_tree[i]
    mid = (l+r)//2
    ans = 10**18
    if jobl<=mid:
        ans = min(ans,query(jobl,jobr,l,mid,i<<1))
    if jobr>mid:
        ans = min(ans,query(jobl,jobr,mid+1,r,i<<1|1))
    return ans

build(0,n-1,1)
st = []
res = [0]*n
for i,x in enumerate(arr):
    while st and arr[st[-1]]<x:
        res[st.pop()] = i
    st.append(i)
op = 0
for i,j in enumerate(res):
    if i>=j:continue
    op+=query(i,j,0,n-1,1)
print(op)