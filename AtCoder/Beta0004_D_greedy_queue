#https://atcoder.jp/contests/awc0004/tasks/awc0004_d
#贪心+优先队列

import heapq
import sys

def solve():
    # 读取输入
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    iterator = iter(data)
    N = int(next(iterator))
    M = int(next(iterator))
    
    # 记录每辆车的区间
    # events[i] 存储所有从车位 i 开始的车的 R 值
    # 这里的 i 范围是 1 到 N
    events = [[] for _ in range(N + 2)]
    
    for _ in range(M):
        l = int(next(iterator))
        r = int(next(iterator))
        events[l].append(r)
    
    min_heap = []
    cars_parked = 0
    
    # 遍历每一个车位
    for x in range(1, N + 1):
        # 1. 将所有从当前位置 x 开始的车加入堆
        for r in events[x]:
            heapq.heappush(min_heap, r)
        
        # 2. 检查堆顶元素是否已经失效
        # 如果堆顶车的右边界 R < x，说明这辆车只能停在 x 之前，但现在已经到 x 了还没停，失败
        # 注意：实际上如果我们严格执行"每个车位安排一辆"，
        # 只要堆里有失效的，其实在之前的步骤就会发现或者在这里发现。
        # 更严格的逻辑是：每次弹出一个给当前位置，如果弹出的那个 R < x，则不可能。
        
        # 贪心策略：给当前车位 x 安排 R 最小的一辆车
        if min_heap:
            r_limit = heapq.heappop(min_heap)
            if r_limit < x:
                print("No")
                return
            cars_parked += 1
    
    # 最后检查是否所有车都停好了
    # 注意：如果 M > N，肯定 No，但题目没说 M <= N
    # 我们的循环只走了 N 步，最多停 N 辆车
    if cars_parked < M:
        print("No")
    else:
        print("Yes")

solve()