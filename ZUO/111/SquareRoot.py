# 一段范围上，每个数字进行开方操作之后，范围的累加和信息并不能够快速得到
# 本题不满足经典线段树范围修改功能的要求，回顾一下上节课内容
# 一个数字即便是最大值10^12，也就开方6次，就会向下取整变成1，以后再也不需要执行开方
# 需要势能分析来评估复杂度，还有剪枝的重要性，一般的剪枝只是优化常数时间，这里要重要的多
# 线段树的区间最值操作，还会用到势能分析

import sys
import math

def solve():
    n = int(sys.stdin.read().strip())
    arr = list(map(int,sys.stdin.read().strip()))
    m = int(sys.stdin.read().strip())
    ops = []
    
    
    tree_sum = [0]*(n<<2)
    tree_max = [0]*(n<<2)

    def up(i):
        tree_sum[i] = tree_sum[i << 1] + tree_sum[i << 1 | 1]
        tree_max[i] = max(tree_max[i << 1], tree_max[i << 1 | 1])
    
    def build(l,r,i):
        if l==r:
            tree_sum[i] = arr[l]
            tree_max[i] = arr[l]
        else:
            mid = (l + r) >> 1
            build(l, mid, i << 1)
            build(mid + 1, r, i << 1 | 1)
            up(i)
    def update(jobl,jobr,l,r,i):
        if tree_max[i] <= 1:
            return
        if l==r:
            val = int(math.isqrt(tree_sum[i]))
            tree_sum[i] = val
            tree_max[i] = val
            return
        
        mid = (l+r)>>1
        if jobl <= mid:
            update(jobl, jobr, l, mid, i << 1)
        if jobr > mid:
            update(jobl, jobr, mid + 1, r, i << 1 | 1)
        up(i)
    
    def query(jobl, jobr, l, r, i):
        if jobl <= l and r <= jobr:
            return tree_sum[i]
        
        mid = (l + r) >> 1
        ans = 0
        if jobl <= mid:
            ans += query(jobl, jobr, l, mid, i << 1)
        if jobr > mid:
            ans += query(jobl, jobr, mid + 1, r, i << 1 | 1)
        return ans

    build(1,n,1)
    results = []
    for _ in range(m):
        op,l,r = map(int,sys.stdin.read().strip())
        if l > r:
            l, r = r, l
        if op==0:
            update(l, r, 1, n, 1)
        else:
            results.append(str(query(l, r, 1, n, 1)))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()