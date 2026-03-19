import heapq

class Solution:
    def mincostToHireWorkers(self, quality, wage, k):
        n = len(quality)
        
        # 构造 (ratio, quality)
        employees = [(wage[i] / quality[i], quality[i]) for i in range(n)]
        
        # 按 ratio 从小到大排序
        employees.sort()
        
        # 最大堆（用负数实现）
        max_heap = []
        quality_sum = 0
        ans = float('inf')
        
        for ratio, q in employees:
            if len(max_heap) < k:
                heapq.heappush(max_heap, -q)
                quality_sum += q
                
                if len(max_heap) == k:
                    ans = min(ans, quality_sum * ratio)
            else:
                # 如果当前质量更小，替换堆顶（最大的质量）
                if -max_heap[0] > q:
                    quality_sum += q + heapq.heappop(max_heap)  # 注意 pop 出来是负数
                    heapq.heappush(max_heap, -q)
                    ans = min(ans, quality_sum * ratio)
        
        return ans