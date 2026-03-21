import sys

MAXN = 100005
LOW = -2000000000

sum_tree = [0] * (MAXN<<2)
max_tree = [0] * (MAXN<<2)
cnt_tree = [0] * (MAXN<<2)
sem_tree = [0] * (MAXN<<2)

def up(i):
    l,r = i<<1,i<<1|1
    sum_tree[i] = sum_tree[l] + sum_tree[r]

    #合并最大值相关信息
    if max_tree[l] > max_tree[r]:
        max_tree[i] = max_tree[l]
        cnt_tree[i] = cnt_tree[l]
        sem_tree[i] = max(sem_tree[l], max_tree[r])
    elif max_tree[l] < max_tree[r]:
        max_tree[i] = max_tree[r]
        cnt_tree[i] = cnt_tree[r]
        sem_tree[i] = max(sem_tree[r], max_tree[l])
    else:
        max_tree[i] = max_tree[l]
        cnt_tree[i] = cnt_tree[l] + cnt_tree[r]
        sem_tree[i] = max(sem_tree[l], sem_tree[r])

def apply_min(i,v):
    """
    核心优化：仅当 v 小于当前最大值时更新。
    由于 Segment Tree Beats 保证了 v > sem_tree[i]，
    所以此操作只会影响 max_tree，不会改变次大值。
    """
    if v < max_tree[i]:
        sum_tree[i] -= cnt_tree[i] * (max_tree[i] - v)
        max_tree[i] = v

def down(i):
    apply_min(i << 1, max_tree[i])
    apply_min(i << 1 | 1, max_tree[i])

def build(l,r,i):
    if l==r:
        max_tree[i] = nums[i]
        cnt_tree[i] = 1
        sem_tree[i] = LOW
        return
    mid = (l + r) >> 1
    build(l, mid, i << 1)
    build(mid + 1, r, i << 1 | 1)
    up(i)

def set_min(jobl, jobr, jobv, l, r, i):
    # 剪枝 1: 当前区间最大值已经小于等于 jobv，无需任何操作
    if max_tree[i] <= jobv:
        return
    # 剪枝 2: 如果 jobv 处于最大值和严格次大值之间，可直接更新并停止递归
    if jobl<=l and jobr<=r and sem_tree[i] < jobv:
        apply_min(i, jobv)
        return
    down(i)
    mid = (l + r) >> 1
    if jobl <= mid:
        set_min(jobl, jobr, jobv, l, mid, i << 1)
    if jobr > mid:
        set_min(jobl, jobr, jobv, mid + 1, r, i << 1 | 1)
    up(i)

def query_max(jobl, jobr, l, r, i):
    if jobl <= l and jobr >= r:
        return max_tree[i]
    down(i)
    mid = (l + r) >> 1
    ans = LOW
    if jobl <= mid:
        ans = max(ans, query_max(jobl, jobr, l, mid, i << 1))
    if jobr > mid:
        ans = max(ans, query_max(jobl, jobr, mid + 1, r, i << 1 | 1))
    
    return ans

def query_sum(jobl, jobr, l, r, i):
    if jobl <= l and jobr >= r:
        return sum_tree[i]
    down(i)
    mid = (l + r) >> 1
    ans = 0
    if jobl <= mid:
        ans += query_sum(jobl, jobr, l, mid, i << 1)
    if jobr > mid:
        ans += query_sum(jobl,jobr,mid+1,r,i<<1|1)
    return ans