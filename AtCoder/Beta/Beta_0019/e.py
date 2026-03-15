#新的知识点，反悔贪心,相邻交换法证明贪心也挺重要的
import heapq
import sys

def solve():
    # 读取输入
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    boxes = []
    idx = 1
    for _ in range(n):
        w = int(input_data[idx])
        d = int(input_data[idx+1])
        # 存储重量 w, 容量 d, 以及它们的和 w+d 用于排序
        boxes.append((w, d, w + d))
        idx += 2

    # 1. 核心贪心策略：按照 W + D 从小到大排序
    # 这决定了箱子从上往下堆叠的理想顺序
    boxes.sort(key=lambda x: x[2])

    pq = [] # 大根堆（存储负的重量，模拟大根堆）
    current_weight = 0 # 当前已选箱子的总重量

    for w, d, _ in boxes:
        # 2. 如果当前已选的总重量不超过该箱子的容量
        # 说明该箱子可以放在最下面
        if current_weight <= d:
            heapq.heappush(pq, -w)
            current_weight += w
        # 3. 反悔贪心：如果放不下，但当前箱子比堆里最重的那个要轻
        # 替换它，使得总数量不变，但总重量 current_weight 减小，为后面留出空间
        elif pq and -pq[0] > w:
            heaviest = -heapq.heappop(pq)
            current_weight = current_weight - heaviest + w
            heapq.heappush(pq, -w)

    # 最终堆的大小就是选出的最大箱子数量
    print(len(pq))

if __name__ == "__main__":
    solve()