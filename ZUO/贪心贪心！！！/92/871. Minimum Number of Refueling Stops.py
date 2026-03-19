

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel>=target:
            return 0
        
        stations.sort(key = lambda x:x[0])

        op = 0
        s = startFuel
        i = 0
        n = len(stations)
        h = []
        while s<target:
            while i<n and stations[i][0]<=s:
                heappush(h,-stations[i][1])
                i+=1
            if not h:
                return -1
            s-=heappop(h)
            op+=1
        return op