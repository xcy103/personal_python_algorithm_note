# 范围修改才需要懒更新机制，单调修改不需要
import sys

arr = []
MAXN = 100005<<2

tree_sum = [0]*MAXN
len0 = [0]*MAXN
pre0 = [0]*MAXN
suf0 = [0]*MAXN
len1 = [0]*MAXN
pre1 = [0]*MAXN
suf1 = [0]*MAXN

change = [0]*MAXN
update = [0]*MAXN
reverse_tag = [0]*MAXN

def up(i,ln,rn):
    l,r = i<<1,i<<1|1
    tree_sum[i] = tree_sum[l] + tree_sum[r]

    len0[i] = max(len0[l],len0[r],suf0[l]+pre0[r])  
    pre0[i] = pre0[l] if pre0[l]<ln else pre0[l]+pre0[r]
    suf0[i] = suf0[r] if suf0[r]<rn else suf0[l]+suf0[r]
    len1[i] = max(len1[l],len1[r],suf1[l]+pre1[r])
    pre1[i] = pre1[l] if pre1[l]<ln else pre1[l]+pre1[r]
    suf1[i] = suf1[r] if suf1[r]<rn else suf1[l]+suf1[r]

def update_lazy(i,v,n):
    tree_sum[i] = v * n 
    v0 = n if v==0 else 0 
    v1 = n if v==1 else 0
    len0[i] = pre0[i] = suf0[i] = v0
    len1[i] = pre1[i] = suf1[i] = v1

    change[i] = v
    update[i] = True
    reverse_tag[i] = False

def reverse_lazy(i,n):
    tree_sum[i] = n - tree_sum[i]
    len0[i],len1[i] = len1[i],len0[i]
    pre0[i],pre1[i] = pre1[i],pre0[i]
    suf0[i],suf1[i] = suf1[i],suf0[i]

    reverse_tag[i] = not reverse_tag[i]

def down(i,ln,rn):
    if update[i]:
        update_lazy(i<<1,change[i],ln)
        update_lazy(i<<1|1,change[i],rn)
        update[i] = False
    if reverse_tag[i]:
        reverse_lazy(i<<1,ln)
        reverse_lazy(i<<1|1,rn)
        reverse_tag[i] = False

def build(l,r,i):
    if l==r:
        tree_sum[i] = arr[l-1]
        pre0[i] = suf0[i] = len0[i] = 1 if arr[l-1]==0 else 0
        pre1[i] = suf1[i] = len1[i] = 1 if arr[l-1]==1 else 0
        return
    else:
        mid = (l + r) >> 1
        build(l, mid, i << 1)
        build(mid + 1, r, i << 1 | 1)
        up(i,mid-l+1,r-mid)

def update(jobl,jobr,jobv,l,r,i):
    if jobl <= l and r <= jobr:
        update_lazy(i,jobv,r-l+1)
        return
    mid = (l + r) >> 1
    down(i,mid-l+1,r-mid)
    if jobl <= mid:
        update(jobl,jobr,jobv,l,mid,i<<1)
    if jobr > mid:
        update(jobl,jobr,jobv,mid+1,r,i<<1|1)
    up(i,mid - l + 1, r - mid)

def reverse_range(jobl,jobr,l,r,i):
    if jobl <= l and r <= jobr:
        reverse_lazy(i,r-l+1)
        return
    mid = (l + r) >> 1
    down(i,mid-l+1,r-mid)
    if jobl <= mid:
        reverse_range(jobl,jobr,l,mid,i<<1)
    if jobr > mid:
        reverse_range(jobl,jobr,mid+1,r,i<<1|1)
    up(i,mid - l + 1, r - mid)

def query_sum(jobl,jobr,l,r,i):
    if jobl <= l and r <= jobr:
        return tree_sum[i]
    mid = (l + r) >> 1
    down(i,mid-l+1,r-mid)
    ans = 0
    if jobl <= mid:
        ans += query_sum(jobl,jobr,l,mid,i<<1)
    if jobr > mid:
        ans += query_sum(jobl,jobr,mid+1,r,i<<1|1)
    
    return ans

def query_len1(jobl,jobr,l,r,i):
    if jobl<= l and r <= jobr:
        return len1[i],pre1[i],suf1[i]
    mid = (l + r) >> 1
    down(i,mid-l+1,r-mid)
    if jobr<=mid:
        return query_len1(jobl,jobr,l,mid,i<<1)
    if jobl>mid:
        return query_len1(jobl,jobr,mid+1,r,i<<1|1)
    
    llen1,lpre1,lsuf1 = query_len1(jobl,jobr,l,mid,i<<1)
    rlen1,rpre1,rsuf1 = query_len1(jobl,jobr,mid+1,r,i<<1|1)
    len1 = max(llen1,rlen1,lsuf1+rpre1)
    pre1 = lpre1 if lpre1<mid-l+1 else lpre1+rpre1
    suf1 = rsuf1 if rsuf1<r-mid else rsuf1+lsuf1

    return len1,pre1,suf1
