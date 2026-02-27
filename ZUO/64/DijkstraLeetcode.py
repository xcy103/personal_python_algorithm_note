# dj算法是处理源点到每个点的最短路问题，也叫单源最短路
# 适用范围是，有向图(无向图)，边的权值没有负数
# 大部分可以直接用普通堆实现dj算法，更快的则是反向索引堆

#两个核心，弹出过的点，忽略，一旦弹出过，最短距离就确定了
# 没有弹出过的点，处理它的所有边，然后只受理让其他没有弹出过的节点距离变小的边
# 左老师是用vis记录一个点是否从小根堆里弹出过
# 灵老师是直接用dis表了

#普通堆实现dj算法复杂度是O(M*LOGM)（M是边的数量）
#测试链接 : https://leetcode.cn/problems/network-delay-time


import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, s: int) -> int:
        # 建图
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # 距离数组
        dist = [float('inf')] * (n + 1)
        dist[s] = 0
        
        visited = [False] * (n + 1)
        
        # 小根堆 (当前距离, 当前节点)
        heap = [(0, s)]
        
        while heap:
            cur_dist, u = heapq.heappop(heap)
            
            if visited[u]:
                continue
            visited[u] = True
            
            for v, w in graph[u]:
                if not visited[v] and cur_dist + w < dist[v]:
                    dist[v] = cur_dist + w
                    heapq.heappush(heap, (dist[v], v))
        
        ans = max(dist[1:])
        return -1 if ans == float('inf') else ans