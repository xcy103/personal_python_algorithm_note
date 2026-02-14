from typing import List

class FallingSquares:
    def __init__(self, size):
        self.n = size
        # 线段树相关数组，4倍空间
        self.max_h = [0] * (self.n << 2)
        self.change = [0] * (self.n << 2)
        self.update_tag = [False] * (self.n << 2)

    def up(self, i):
        self.max_h[i] = max(self.max_h[i << 1], self.max_h[i << 1 | 1])

    def down(self, i):
        if self.update_tag[i]:
            self.lazy(i << 1, self.change[i])
            self.lazy(i << 1 | 1, self.change[i])
            self.update_tag[i] = False

    def lazy(self, i, v):
        self.update_tag[i] = True
        self.change[i] = v
        self.max_h[i] = v

    def update(self, jobl, jobr, jobv, l, r, i):
        if jobl <= l and r <= jobr:
            self.lazy(i, jobv)
            return
        
        mid = (l + r) >> 1
        self._push_down(i)
        if jobl <= mid:
            self.update(jobl, jobr, jobv, l, mid, i << 1)
        if jobr > mid:
            self.update(jobl, jobr, jobv, mid + 1, r, i << 1 | 1)
        self._push_up(i)

    def query(self, jobl, jobr, l, r, i):
        if jobl <= l and r <= jobr:
            return self.max_h[i]
        
        mid = (l + r) >> 1
        self._push_down(i)
        ans = 0
        if jobl <= mid:
            ans = max(ans, self.query(jobl, jobr, l, mid, i << 1))
        if jobr > mid:
            ans = max(ans, self.query(jobl, jobr, mid + 1, r, i << 1 | 1))
        return ans

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        # 1. 离散化坐标
        coords = set()
        for left, length in positions:
            coords.add(left)
            coords.add(left + length - 1)
        
        # 排序并映射
        sorted_coords = sorted(list(coords))
        rank_map = {val: i + 1 for i, val in enumerate(sorted_coords)}
        n = len(sorted_coords)

        # 2. 初始化线段树
        st = FallingSquares(n)
        
        ans = []
        current_max = 0
        
        # 3. 模拟掉落过程
        for left, length in positions:
            l = rank_map[left]
            r = rank_map[left + length - 1]
            
            # 查询当前范围内的最大高度
            h = st.query(l, r, 1, n, 1) + length
            # 更新该范围的高度
            st.update(l, r, h, 1, n, 1)
            
            current_max = max(current_max, h)
            ans.append(current_max)
            
        return ans