import sys

MAXN = 50005

pre = [0]*(MAXN<<2)
suf = [0]*(MAXN<<2)
h = []

def up(l,r,i):
    mid = (l+r)>>1
    ln = mid-l+1
    rn = r-mid
    left = i<<1
    right = i<<1|1

    pre[i] = pre[left]
    suf[i] = suf[right]
    if pre[left]==ln:
        pre[i]+=pre[right]
    if suf[right]==rn:
        suf[i]+=suf[left]

def build(l,r,i):
    if l==r:
        pre[i] = 1
        suf[i] = 1
        return
    mid = (l+r)>>1
    build(l,mid,i<<1)
    build(mid+1,r,1<<1|1)
    up(l,r,i)

def update(jobi,jobv,l,r,i):
    if l==r:
        pre[i] = suf[i] = jobv
    else:
        mid = (l+r)>>1
        if jobi<=mid:
            update(jobi,jobv,l,mid,i<<1)
        else:
            update(jobi,jobv,mid+1,r,i<<1|1)
        up(l,r,i)

def query(jobi,jobv,l,r,i):
    if l==r:
        return pre[i]
    mid = (l+r)>>1
    if jobi<=mid:
        if jobi>=mid-suf[i<<1]+1:
            return suf[i<<1] + pre[i<<1|1]
        else:
            return query(jobi,jobv,l,mid,i<<1)
    else:
        if jobi<=pre[i<<1|1] + mid:
            return suf[i<<1] + pre[i<<1|1]
        else:
            return query(jobi,jobv,mid+1,r,i<<1|1)
