import sys
import heapq
from collections import defaultdict

def solve():
    # 提高输入读取效率
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    Q = int(data[0])
    
    # left_heap 是大顶堆，Python 默认是小顶堆，所以存负数
    left_heap = []
    # right_heap 是小顶堆，正常存正数
    right_heap = []
    
    # 记录每个堆中有效元素的实际数量
    left_size = 0
    right_size = 0
    
    # 延迟删除计数器
    del_counts = defaultdict(int)
    
    median_hits = 0
    
    # 辅助函数：清除堆顶已被标记删除的无效元素
    def clean_left():
        while left_heap:
            val = -left_heap[0]
            if del_counts[val] > 0:
                heapq.heappop(left_heap)
                del_counts[val] -= 1
            else:
                break

    def clean_right():
        while right_heap:
            val = right_heap[0]
            if del_counts[val] > 0:
                heapq.heappop(right_heap)
                del_counts[val] -= 1
            else:
                break

    # 辅助函数：平衡两个堆的大小，保证 left_size == (total + 1) // 2
    def balance():
        nonlocal left_size, right_size
        total = left_size + right_size
        target_left = (total + 1) // 2
        
        while left_size < target_left:
            clean_right()
            val = heapq.heappop(right_heap)
            heapq.heappush(left_heap, -val)
            left_size += 1
            right_size -= 1
            
        while left_size > target_left:
            clean_left()
            val = -heapq.heappop(left_heap)
            heapq.heappush(right_heap, val)
            left_size -= 1
            right_size += 1

    idx = 1
    for _ in range(Q):
        op = data[idx]
        X = int(data[idx+1])
        idx += 2
        
        if op == '+':
            # 插入操作
            if not left_heap or X <= -left_heap[0]:
                heapq.heappush(left_heap, -X)
                left_size += 1
            else:
                heapq.heappush(right_heap, X)
                right_size += 1
            balance()
            
        elif op == '-':
            # 删除操作前，先通过 clean 获取当前真实的中位数
            clean_left()
            current_median = -left_heap[0]
            
            # 判断是否命中中位数
            if X == current_median:
                median_hits += 1
            
            # 标记删除
            del_counts[X] += 1
            
            # 看看这个 X 属于哪一部分，更新对应的有效大小
            if X <= current_median:
                left_size -= 1
            else:
                right_size -= 1
                
            # 重新平衡堆
            balance()

    print(median_hits)

if __name__ == '__main__':
    solve()