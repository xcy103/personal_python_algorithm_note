#没有次大值，就没有标签了
# 标签的数量是有限的，O(n)个，每次下扎就会回收一个标签
# 下闸的带就是O(logn)
import sys

# 增加递归深度以处理深层线段树
sys.setrecursionlimit(1000000)

MAXN = 500001
LOWEST = -float('inf')

# 线段树核心数组
arr = [0] * MAXN
sum_tree = [0] * (MAXN << 2)
max_tree = [0] * (MAXN << 2)
cnt_tree = [0] * (MAXN << 2)
sem_tree = [LOWEST] * (MAXN << 2)
max_add = [0] * (MAXN << 2)
other_add = [0] * (MAXN << 2)

def up(i):
    l, r = i << 1, i << 1 | 1
    sum_tree[i] = sum_tree[l] + sum_tree[r]
    max_tree[i] = max(max_tree[l], max_tree[r])
    
    if max_tree[l] > max_tree[r]:
        cnt_tree[i] = cnt_tree[l]
        sem_tree[i] = max(sem_tree[l], max_tree[r])
    elif max_tree[l] < max_tree[r]:
        cnt_tree[i] = cnt_tree[r]
        sem_tree[i] = max(max_tree[l], sem_tree[r])
    else:
        cnt_tree[i] = cnt_tree[l] + cnt_tree[r]
        sem_tree[i] = max(sem_tree[l], sem_tree[r])

def lazy(i, n, max_v, other_v):
    # n 为区间长度
    sum_tree[i] += max_v * cnt_tree[i] + other_v * (n - cnt_tree[i])
    max_tree[i] += max_v
    if sem_tree[i] != LOWEST:
        sem_tree[i] += other_v
    max_add[i] += max_v
    other_add[i] += other_v

def down(i, ln, rn):
    l, r = i << 1, i << 1 | 1
    # 通过子节点最大值判断谁属于父节点之前的“最大值群体”
    tmp = max(max_tree[l], max_tree[r])
    
    # 左孩子下传
    if max_tree[l] == tmp:
        lazy(l, ln, max_add[i], other_add[i])
    else:
        lazy(l, ln, other_add[i], other_add[i])
        
    # 右孩子下传
    if max_tree[r] == tmp:
        lazy(r, rn, max_add[i], other_add[i])
    else:
        lazy(r, rn, other_add[i], other_add[i])
        
    max_add[i] = 0
    other_add[i] = 0

def build(l, r, i):
    max_add[i] = 0
    other_add[i] = 0
    if l == r:
        sum_tree[i] = max_tree[i] = arr[l]
        sem_tree[i] = LOWEST
        cnt_tree[i] = 1
    else:
        mid = (l + r) >> 1
        build(l, mid, i << 1)
        build(mid + 1, r, i << 1 | 1)
        up(i)

def add(jobl, jobr, jobv, l, r, i):
    if jobl <= l and r <= jobr:
        lazy(i, r - l + 1, jobv, jobv)
    else:
        mid = (l + r) >> 1
        down(i, mid - l + 1, r - mid)
        if jobl <= mid:
            add(jobl, jobr, jobv, l, mid, i << 1)
        if jobr > mid:
            add(jobl, jobr, jobv, mid + 1, r, i << 1 | 1)
        up(i)

def set_min(jobl, jobr, jobv, l, r, i):
    if jobv >= max_tree[i]:
        return
    # Segment Tree Beats 核心判断：jobv 在最大值和次大值之间
    if jobl <= l and r <= jobr and sem_tree[i] < jobv:
        lazy(i, r - l + 1, jobv - max_tree[i], 0)
    else:
        mid = (l + r) >> 1
        down(i, mid - l + 1, r - mid)
        if jobl <= mid:
            set_min(jobl, jobr, jobv, l, mid, i << 1)
        if jobr > mid:
            set_min(jobl, jobr, jobv, mid + 1, r, i << 1 | 1)
        up(i)

def query_sum(jobl, jobr, l, r, i):
    if jobl <= l and r <= jobr:
        return sum_tree[i]
    mid = (l + r) >> 1
    down(i, mid - l + 1, r - mid)
    res = 0
    if jobl <= mid:
        res += query_sum(jobl, jobr, l, mid, i << 1)
    if jobr > mid:
        res += query_sum(jobl, jobr, mid + 1, r, i << 1 | 1)
    return res

def query_max(jobl, jobr, l, r, i):
    if jobl <= l and r <= jobr:
        return max_tree[i]
    mid = (l + r) >> 1
    down(i, mid - l + 1, r - mid)
    res = LOWEST
    if jobl <= mid:
        res = max(res, query_max(jobl, jobr, l, mid, i << 1))
    if jobr > mid:
        res = max(res, query_max(jobl, jobr, mid + 1, r, i << 1 | 1))
    return res