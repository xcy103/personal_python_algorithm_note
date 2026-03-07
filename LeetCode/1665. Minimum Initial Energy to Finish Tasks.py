#这道题排序策略是按 (minimum - actual) 排序
#假如A = [1,10],B = [5,6] 先做A，只需要10；先做B则需要15


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        
        tasks.sort(key=lambda x: x[1]-x[0], reverse=True)

        energy = 0
        cur = 0

        for actual, minimum in tasks:
            
            if cur < minimum:
                energy += minimum - cur
                cur = minimum
            
            cur -= actual

        return energy