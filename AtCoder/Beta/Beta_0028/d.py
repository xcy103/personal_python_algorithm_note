import sys
import heapq
#这里比较巧的是，用了堆，不是平时用的队列
def solve():
    # 使用 fast I/O
    input = sys.stdin.read().split()
    if not input:
        return
    
    n = int(input[0])
    m = int(input[1])
    
    g = [[] for _ in range(n + 1)]
    ind = [0] * (n + 1)
    
    # 填充邻接表和入度数组
    ptr = 2
    for _ in range(m):
        a = int(input[ptr])
        b = int(input[ptr+1])
        g[a].append(b)
        ind[b] += 1
        ptr += 2
        
    # 1. 找出所有初始入度为 0 的节点，放入优先队列（最小堆）
    pq = []
    for i in range(1, n + 1):
        if ind[i] == 0:
            heapq.heappush(pq, i)
            
    res = []
    
    # 2. 开始拓扑排序
    while pq:
        # 弹出当前可选课程中编号最小的
        cur = heapq.heappop(pq)
        res.append(str(cur))
        
        for nxt in g[cur]:
            ind[nxt] -= 1
            # 当下游课程的所有前置课都修完了，加入堆
            if ind[nxt] == 0:
                heapq.heappush(pq, nxt)
                
    # 3. 输出结果
    print(' '.join(res))

if __name__ == "__main__":
    solve()