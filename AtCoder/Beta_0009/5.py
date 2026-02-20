import sys

# data = sys.stdin.read().split()
# ptr = 0
# n,q = int(data[ptr]),int(data[ptr+1])
# ptr+=2
# arr = [0]*n
# queries = []
# for _ in range(n):
#     arr.append(int(data[ptr]))
#     ptr+=1
# for _ in range(q):
#     l,r = int(data[ptr]),int(data[ptr+1])
#     queries.append((l,r))
#     ptr+=2
n,q = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
queries = []
for _ in range(q):
    l,r = map(int,sys.stdin.readline().split())
    queries.append((l,r))
max_tree = [0]*(n<<2)
min_tree = [0]*(n<<2)

def build(i,l,r):
    if l==r:
        max_tree[i] = arr[l]
        min_tree[i] = arr[l]
        return
    mid = (l+r)>>1
    build(i<<1,l,mid)
    build(i<<1|1,mid+1,r)
    max_tree[i] = max(max_tree[i<<1],max_tree[i<<1|1])
    min_tree[i] = min(min_tree[i<<1],min_tree[i<<1|1])

def query(jobl,jobr,l,r,i):
    if jobl<=l and r<=jobr:
        return max_tree[i],min_tree[i]
    mid = (l+r)>>1
    ret_max,ret_min = float('-inf'),float('inf')
    if jobl<=mid:
        tmp_max,tmp_min = query(jobl,jobr,l,mid,i<<1)
        ret_max = max(ret_max,tmp_max)
        ret_min = min(ret_min,tmp_min)
    if mid<jobr:
        tmp_max,tmp_min = query(jobl,jobr,mid+1,r,i<<1|1)
        ret_max = max(ret_max,tmp_max)
        ret_min = min(ret_min,tmp_min)
    return ret_max,ret_min

build(1,0,n-1)
ans = []
for l,r in queries:
    max_val,min_val = query(l-1,r-1,0,n-1,1)
    ans.append(max_val-min_val)

print('\n'.join(map(str,ans)))