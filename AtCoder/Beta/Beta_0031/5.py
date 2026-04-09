"""
PROBLEM: Power Grid Blackout Crisis (E - 466 pts)

[1. 核心模型：最大流 (Max Flow)]
这是一个典型的“供需平衡”问题，可以用网络流建模：
- 源点 (Source): 连接所有【发电站】。
- 汇点 (Sink): 连接所有【工厂】。
- 传输线: 双向边，容量为 Cj。
- 发电站: 节点容量 Wk。
- 工厂: 需求容量 Bi。

[2. 网络流建模图示]
(S) --Wk--> [Power Plant k] --Cj--> [Location U/V] --Bi--> (T)

具体连边：
1. Source -> Power Plant k: 容量 Wk (如果该电站未损坏)。
2. Location U <-> Location V: 双向边，容量均为 Cj。
3. Factory i -> Sink: 容量 Bi。

[3. 判定条件]
所有工厂的总需求 Total_Demand = sum(Bi)。
如果在当前状态下，从源点到汇点的【最大流】 == Total_Demand，则输出 "Yes"，否则 "No"。

[4. 优化：动态删点 -> 逆向加点]
由于发电站会顺序损坏 (Q 个事件)，每次重新跑最大流太慢。
- 策略：将损坏过程【反过来】看。
- 从最后一次损坏后的状态开始，逐个【修复】(添加) 发电站。
- 使用 Dinic 算法或 ISAP，在残量网络上直接增广，这样效率极高。

[5. 算法复杂度]
- 节点数 V = N + K + 2 (约 70)
- 边数 E = M + N + K (约 400)
- 修复次数 Q (约 30)
- 最大流在稀疏小图上速度飞快。
"""

import sys

# 增加递归深度，防止 Dinic 的 DFS 溢出
sys.setrecursionlimit(2000)

class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.level = []

    def add_edge(self, u, v, cap):
        # 记录边及其反向边在 graph[v] 中的索引
        self.graph[u].append([v, cap, len(self.graph[v])])
        self.graph[v].append([u, 0, len(self.graph[u]) - 1])

    def bfs(self, s, t):
        self.level = [-1] * self.n
        self.level[s] = 0
        queue = [s]
        while queue:
            u = queue.pop(0)
            for v, cap, rev in self.graph[u]:
                if cap > 0 and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1
                    queue.append(v)
        return self.level[t] >= 0

    def dfs(self, u, t, flow, ptr):
        if u == t or flow == 0:
            return flow
        for i in range(ptr[u], len(self.graph[u])):
            ptr[u] = i
            v, cap, rev = self.graph[u][i]
            if self.level[v] == self.level[u] + 1 and cap > 0:
                pushed = self.dfs(v, t, min(flow, cap), ptr)
                if pushed > 0:
                    self.graph[u][i][1] -= pushed
                    self.graph[v][rev][1] += pushed
                    return pushed
        return 0

    def max_flow(self, s, t):
        max_f = 0
        while self.bfs(s, t):
            ptr = [0] * self.n
            while True:
                pushed = self.dfs(s, t, float('inf'), ptr)
                if pushed == 0:
                    break
                max_f += pushed
        return max_f

def solve():
    # 读入基础数据
    input = sys.stdin.read().split()
    if not input: return
    idx = 0
    N, K, M = int(input[idx]), int(input[idx+1]), int(input[idx+2]); idx += 3
    
    B = [int(input[idx+i]) for i in range(N)]; idx += N
    W = [int(input[idx+i]) for i in range(K)]; idx += K
    
    edges = []
    for _ in range(M):
        u, v, c = map(int, input[idx:idx+3]); idx += 3
        edges.append((u-1, v-1, c))
    
    Q = int(input[idx]); idx += 1
    S = [int(input[idx+i]) - 1 for i in range(Q)]; idx += Q

    # 建模准备
    source = N + K
    sink = N + K + 1
    dinic = Dinic(N + K + 2)
    
    # 1. 工厂到汇点的边 (固定)
    total_demand = sum(B)
    for i in range(N):
        dinic.add_edge(i, sink, B[i])
        
    # 2. 传输线双向边 (固定)
    for u, v, c in edges:
        dinic.add_edge(u, v, c)
        dinic.add_edge(v, u, c)
        
    # 3. 处理电站状态
    broken = [False] * K
    for s_idx in S:
        broken[s_idx] = True
        
    # 记录电站到源点的边索引，方便后续“修复”
    plant_edges = {}
    for k in range(K):
        # 即使是坏的电站，我们也先建边，容量初始为 0
        plant_node = N + k
        cap = 0 if broken[k] else W[k]
        # 保存这个 edge 的引用位置
        plant_edges[k] = len(dinic.graph[source])
        dinic.add_edge(source, plant_node, cap)

    # 4. 逆向加点
    results = []
    current_flow = dinic.max_flow(source, sink)
    
    # 倒序处理 Q 个事件
    for i in range(Q - 1, -1, -1):
        results.append("Yes" if current_flow == total_demand else "No")
        # 修复电站 S[i]
        repair_k = S[i]
        # 找到对应边并修改容量 (直接在残量网络上操作)
        for edge_info in dinic.graph[source]:
            if edge_info[0] == N + repair_k:
                edge_info[1] = W[repair_k] # 恢复容量
                break
        current_flow += dinic.max_flow(source, sink)
        
    # 5. 输出结果 (由于是逆向处理，需要再反过来)
    for res in reversed(results):
        print(res)

if __name__ == "__main__":
    solve()