#整体思路就是，把一个公交站的所有stops看作一个点
#如果一条线路某一个stops 连接其他公交线路，并且尚未访问，就入队
#思考一下，就相当于逐层展开
#切记不能走回头路，需要对于访问过的stops和公交路线标记已访问
# 队列中保存的是公交线路编号，其实也可以用，set标记bus，但是bus很少，建议用数组

from typing import List
from collections import deque,defaultdict 



class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:
            return 0
        n = len(routes)
        stop2bus = defaultdict(list)

        for i,route in enumerate(routes):
            for stop in route:
                stop2bus[stop].append(i)
        
        q = deque()
        vis_bus = [False]*n
        vis_stops = set()
        for bus in stop2bus[source]:
            q.append(bus)
            vis_bus[bus] = True
        step = 1
        while q:
            for _ in range(len(q)):
                bus = q.popleft()
                for stop in routes[bus]:
                    if stop==target:
                        return step

                    if stop in vis_stops:
                        continue
                    
                    for nb in stop2bus[stop]:
                        if not vis_bus[nb]:
                            vis_bus[nb] = True
                            q.append(nb)
            step+=1
        
        return -1