import sys

# 增加递归深度，防止深层递归导致栈溢出
sys.setrecursionlimit(200000)

class SegmentTreeRangeAddMax:
    def __init__(self, size):
        # 数组大小设置，+5 防止越界
        self.MAXN = size + 5
        
        # 原始数组，下标从 1 开始使用
        self.arr = [0] * self.MAXN
        
        # 维护最大值的数组，大小为 4 倍
        # 命名为 max_val 避免与 python 内置 max() 冲突
        self.max_val = [0] * (self.MAXN << 2)
        
        # 懒标记数组：记录累加的值
        self.add = [0] * (self.MAXN << 2)

    # ------------------ 内部辅助方法 ------------------

    # 向上汇总 (Push Up)
    def up(self, i):
        # 当前节点最大值 = max(左孩子最大值, 右孩子最大值)
        self.max_val[i] = max(self.max_val[i << 1], self.max_val[i << 1 | 1])

    # 懒更新的具体动作
    # i: 当前节点下标, v: 增加的值
    def lazy_action(self, i, v):
        self.max_val[i] += v
        self.add[i] += v

    # 懒信息的下发 (Push Down)
    def down(self, i):
        if self.add[i] != 0:
            # 发给左孩子
            self.lazy_action(i << 1, self.add[i])
            # 发给右孩子
            self.lazy_action(i << 1 | 1, self.add[i])
            # 清空当前懒标记
            self.add[i] = 0

    # ------------------ 核心公开方法 ------------------

    # 建树
    # l, r: 当前构建的范围 (通常初始为 1, n)
    # i: 当前节点下标 (通常初始为 1)
    def build(self, l, r, i):
        if l == r:
            self.max_val[i] = self.arr[l]
        else:
            mid = (l + r) >> 1
            self.build(l, mid, i << 1)
            self.build(mid + 1, r, i << 1 | 1)
            self.up(i)
        self.add[i] = 0

    # 范围增加 (Range Add)
    # jobl ~ jobr 范围的所有数字增加 jobv
    def add_range(self, jobl, jobr, jobv, l, r, i):
        if jobl <= l and r <= jobr:
            self.lazy_action(i, jobv)
        else:
            self.down(i)
            mid = (l + r) >> 1
            if jobl <= mid:
                self.add_range(jobl, jobr, jobv, l, mid, i << 1)
            if jobr > mid:
                self.add_range(jobl, jobr, jobv, mid + 1, r, i << 1 | 1)
            self.up(i)

    # 范围查询最大值 (Range Query Max)
    # 查询 jobl ~ jobr 范围的最大值
    def query(self, jobl, jobr, l, r, i):
        if jobl <= l and r <= jobr:
            return self.max_val[i]
        
        self.down(i)
        mid = (l + r) >> 1
        # 初始化为一个极小值，相当于 Java 的 Long.MIN_VALUE
        ans = float('-inf')
        
        if jobl <= mid:
            ans = max(ans, self.query(jobl, jobr, l, mid, i << 1))
        if jobr > mid:
            ans = max(ans, self.query(jobl, jobr, mid + 1, r, i << 1 | 1))
        return ans