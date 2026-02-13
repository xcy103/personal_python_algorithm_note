import sys

# 增加递归深度，防止深层递归栈溢出
sys.setrecursionlimit(200000)

class SegmentTreeUpdateSum:
    def __init__(self, size):
        # 数组大小设置，+5 防止越界
        self.MAXN = size + 5
        
        # 原始数组，下标从 1 开始使用
        self.arr = [0] * self.MAXN
        
        # 线段树维护的累加和数组，大小为 4 倍
        self.sum_arr = [0] * (self.MAXN << 2)
        
        # 懒标记值数组：记录要变成什么数字
        self.change = [0] * (self.MAXN << 2)
        
        # 懒标记状态数组：记录当前节点是否有懒任务
        # 注意：因为要变成的数字可能是 0，所以不能用 change[i] != 0 来判断
        # 必须用一个额外的布尔数组来标记
        self.update_flag = [False] * (self.MAXN << 2)

    # ------------------ 内部辅助方法 ------------------

    # 向上汇总 (Push Up)
    def up(self, i):
        # 父节点和 = 左孩子和 + 右孩子和
        self.sum_arr[i] = self.sum_arr[i << 1] + self.sum_arr[i << 1 | 1]

    # 懒信息的下发 (Push Down)
    def down(self, i, ln, rn):
        # 只有当 update_flag 为 True 时才下发
        if self.update_flag[i]:
            # 发给左孩子
            self.lazy_action(i << 1, self.change[i], ln)
            # 发给右孩子
            self.lazy_action(i << 1 | 1, self.change[i], rn)
            # 任务下发后，当前节点的懒标记清除
            self.update_flag[i] = False

    # 执行懒更新的具体动作
    # i: 当前节点下标, v: 要变成的值, n: 当前节点管辖的数字个数
    def lazy_action(self, i, v, n):
        self.sum_arr[i] = v * n
        self.change[i] = v
        self.update_flag[i] = True

    # ------------------ 核心公开方法 ------------------

    # 建树
    # l, r: 当前构建的范围 (通常初始为 1, n)
    # i: 当前节点下标 (通常初始为 1)
    def build(self, l, r, i):
        if l == r:
            self.sum_arr[i] = self.arr[l]
        else:
            mid = (l + r) >> 1
            self.build(l, mid, i << 1)
            self.build(mid + 1, r, i << 1 | 1)
            self.up(i)
        # 初始化懒标记
        self.change[i] = 0
        self.update_flag[i] = False

    # 范围更新 (Range Update / Set)
    # 将 jobl ~ jobr 范围的所有数字变成 jobv
    def update(self, jobl, jobr, jobv, l, r, i):
        if jobl <= l and r <= jobr:
            self.lazy_action(i, jobv, r - l + 1)
        else:
            mid = (l + r) >> 1
            self.down(i, mid - l + 1, r - mid)
            if jobl <= mid:
                self.update(jobl, jobr, jobv, l, mid, i << 1)
            if jobr > mid:
                self.update(jobl, jobr, jobv, mid + 1, r, i << 1 | 1)
            self.up(i)

    # 范围查询 (Range Query)
    # 查询 jobl ~ jobr 范围的累加和
    def query(self, jobl, jobr, l, r, i):
        if jobl <= l and r <= jobr:
            return self.sum_arr[i]
        
        mid = (l + r) >> 1
        self.down(i, mid - l + 1, r - mid)
        ans = 0
        if jobl <= mid:
            ans += self.query(jobl, jobr, l, mid, i << 1)
        if jobr > mid:
            ans += self.query(jobl, jobr, mid + 1, r, i << 1 | 1)
        return ans