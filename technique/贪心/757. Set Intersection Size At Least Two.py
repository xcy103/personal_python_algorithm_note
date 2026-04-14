class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # 1. 排序：右端点升序；右端点相同时，左端点降序
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        # 初始化：p1, p2 代表集合中最后添加的两个数
        # 初始值设为 -1 是因为区间起点最小是 0
        p1, p2 = -1, -1
        res = 0
        
        for s, e in intervals:
            # 情况 1：区间完全在已知点右侧，需要补 2 个点
            if s > p2:
                res += 2
                p1 = e - 1
                p2 = e
            # 情况 2：区间只覆盖了 p2 这一个点，需要补 1 个点
            elif s > p1:
                res += 1
                # 贪心：如果 p2 已经是 e，为了避开，点要加在 e
                # 但根据排序规则，这里直接让 p1 = p2, p2 = e 即可
                p1 = p2
                p2 = e
            # 情况 3：s <= p1，说明 p1, p2 都在 [s, e] 内，不需要操作
                
        return res