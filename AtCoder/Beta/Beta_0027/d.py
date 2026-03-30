import heapq
import sys

def solve():
    # 使用快速读取，防止 N, M 过大导致输入耗时
    input = sys.stdin.read().split()
    if not input:
        return
    
    N = int(input[0])
    M = int(input[1])
    
    jobs = []
    idx = 2
    for _ in range(N):
        h = int(input[idx])
        s = int(input[idx+1])
        jobs.append((h, s))
        idx += 2
    
    # 工人技能 P
    P = []
    for _ in range(M):
        P.append(int(input[idx]))
        idx += 1
    
    # 1. 排序：门槛低的工作在前，技能弱的工人在前
    jobs.sort() # 按 H_i 升序
    P.sort()    # 按 P_j 升序
    
    max_heap = [] # 存放当前可选工作的销售额 S_i (存负数以模拟最大堆)
    job_ptr = 0
    total_sales = 0
    
    # 2. 遍历每个工人，为其分配最值钱的工作
    for skill in P:
        # 将所有门槛满足当前工人的工作加入堆
        while job_ptr < N and jobs[job_ptr][0] <= skill:
            # 放入销售额 S_i
            heapq.heappush(max_heap, -jobs[job_ptr][1])
            job_ptr += 1
        
        # 如果没有工作能做了，说明无法安排全员
        if not max_heap:
            print("-1")
            return
        
        # 贪心：取走当前能做的最值钱的工作
        total_sales += -heapq.heappop(max_heap)
    
    print(total_sales)

if __name__ == "__main__":
    solve()