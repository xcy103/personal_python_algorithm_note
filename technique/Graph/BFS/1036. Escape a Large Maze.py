from typing import List
from collections import deque
#这道题blocked很小，如果你可以走出超过blocked能围成的最大得面积，就说明你没有被围住
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        
        blocked_set = set(map(tuple, blocked))
        MAX_AREA = len(blocked) * (len(blocked) - 1) // 2  # 最大可能围住的面积
        
        def bfs(start, end):
            visited = set()
            queue = deque([tuple(start)])
            visited.add(tuple(start))
            
            while queue and len(visited) <= MAX_AREA:
                x, y = queue.popleft()
                
                # 找到终点
                if [x, y] == end:
                    return True
                
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < 10**6 and 0 <= ny < 10**6:
                        if (nx, ny) not in blocked_set and (nx, ny) not in visited:
                            visited.add((nx, ny))
                            queue.append((nx, ny))
            
            # 如果访问超过最大围住面积，说明没被围住
            return len(visited) > MAX_AREA
        
        # 必须双向检查
        return bfs(source, target) and bfs(target, source)