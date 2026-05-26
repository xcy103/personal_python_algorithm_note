import sys
# 导入第三方库 SortedList
from sortedcontainers import SortedList

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    Q = int(data[0])
    
    # 初始化有序列表
    sl = SortedList()
    median_hits = 0
    
    idx = 1
    for _ in range(Q):
        op = data[idx]
        X = int(data[idx+1])
        idx += 2
        
        if op == '+':
            sl.add(X)
        elif op == '-':
            # 1. 弹出前，先计算当前集合的大小 n
            n = len(sl)
            
            # 2. 题目定义：1-indexed 排序后的第 ceil(n / 2) 个数
            # 转换为 Python 的 0-indexed 索引就是：(n + 1) // 2 - 1
            median_idx = (n + 1) // 2 - 1
            current_median = sl[median_idx]
            
            # 3. 判断是否命中中位数
            if X == current_median:
                median_hits += 1
                
            # 4. 从有序列表中移除一个 X
            sl.remove(X)
            
    print(median_hits)

if __name__ == '__main__':
    solve()


