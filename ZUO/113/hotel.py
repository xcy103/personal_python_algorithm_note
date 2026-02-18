
import sys

MAXN = 50005

len_tree = [0]*(MAXN<<2)
pre_tree = [0]*(MAXN<<2)
suf_tree = [0]*(MAXN<<2)
change = [0]*(MAXN<<2)
update_tag = [False]*(MAXN<<2)

def up(l,r,i):

    left = i<<1
    right = i<<1|1
    mid = (l+r)>>1
    ln = mid-l+1
    rn = r-mid

    len_tree[i] = max(len_tree[left],len_tree[right],suf_tree[left]+pre_tree[right])
    pre_tree[i] = pre_tree[left]
    suf_tree[i] = suf_tree[right]
    if pre_tree[left]==ln:
        pre_tree[i] += pre_tree[right]
    if suf_tree[right]==rn:
        suf_tree[i] += suf_tree[left]

def lazy(i,n):
    len_tree[i] = pre_tree[i] = suf_tree[i] = n
    change[i] = 0
    update_tag[i] = True

def down(i,ln,rn):
    if update_tag[i]:
        lazy(i<<1,change[i],ln)
        lazy(i<<1|1,change[i],rn)
        update_tag[i] = False

def build(l,r,i):
    if l==r:
        len_tree[i] = pre_tree[i] = suf_tree[i] = 1
        return
    mid = (l+r)>>1
    build(l,mid,i<<1)
    build(mid+1,r,i<<1|1)
    up(l,r,i)

def update(jobl,jobr,l,r,i):
    if jobl <= l and r <= jobr:
        lazy(i,r-l+1)
        return
    mid = (l + r) >> 1
    down(i,mid-l+1,r-mid)
    if jobl <= mid:
        update(jobl,jobr,l,mid,i<<1)
    if jobr > mid:
        update(jobl,jobr,mid+1,r,i<<1|1)
    up(l,r,i)

def query(x,l,r,i):
    if l==r:
        return l
    mid = (l+r)>>1
    down(i,mid-l+1,r-mid)
    if len_tree[i<<1]>=x:
        return query(x,l,mid,i<<1)
    if suf_tree[i<<1] + pre_tree[i<<1|1]>=x:
        return mid - suf_tree[i<<1] + 1
    return query(x,mid+1,r,i<<1|1)
