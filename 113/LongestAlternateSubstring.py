# 这里刚开始没想通，单点修改之后维护的信息怎么修改
# 我懂了，up一下就行了，对于线段树的up方法理解不深

import sys

MAXN = 200005

arr = [0]

len_tree = [0]*(MAXN<<2)
pre_tree = [0]*(MAXN<<2)
suf_tree = [0]*(MAXN<<2)

# 没想明白为什么要传入l,r，我刚开始想的是l，r就是i<<1 和i<<1|1
# 其实不是的，你看下面的reverse或者build函数，l,r可能是mid 和mid+1
# 这个i代表的是这个区间，填在数组什么位置上
def up(i,l,r):
    left,right = i<<1,i<<1|1
    mid = (l+r)>>1
    ln = mid-l+1
    rn = r-mid

    len_tree[i] = max(len_tree[left],len_tree[right])
    pre_tree[i] = pre_tree[left]
    suf_tree[i] = suf_tree[right]

    if arr[mid]!=arr[mid+1]:
        len_tree[i] = max(len_tree[i],suf_tree[left]+pre_tree[right])
        if pre_tree[left]==ln:
            pre_tree[i] = pre_tree[left]+pre_tree[right]
        if suf_tree[right]==rn:
            suf_tree[i] = suf_tree[left]+suf_tree[right]
    

def build(l,r,i):
    if l==r:
        len_tree[i] = 1
        pre_tree[i] = 1
        suf_tree[i] = 1
        return
    mid = (l+r)>>1
    build(l,mid,i<<1)
    build(mid+1,r,i<<1|1)
    up(l,r,i)

def reverse(jobi,l,r,i):
    if l==r:
        arr[jobi]^=1
    else:
        mid = (l+r)>>1
        if jobi <= mid:
            reverse(jobi,l,mid,i<<1)
        else:
            reverse(jobi,mid+1,r,i<<1|1)
        up(l,r,i)
    


    
    

