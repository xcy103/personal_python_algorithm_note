

class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        n = len(receiver)

        power = 0
        while (1<<power) <= k>>1:
            power+=1
        
        kb = []
        tmp = k
        for p in range(power,-1,-1):
            if 1<<p <=tmp:
                kb.append(p)
                tmp-=1<<p
        
        stjump = [[0]*(power+1) for _ in range(n)]
        stsum = [[0]*(power+1) for _ in range(n)]

        for i in range(n):
            stjump[i][0] = receiver[i]
            stsum[i][0] = receiver[i]
        for p in range(1,power+1):
            for i in range(n):
                nxt = stjump[i][p-1]
                stjump[i][p] = stjump[nxt][p-1] 
                stsum[i][p] = stsum[i][p-1] + stsum[nxt][p-1] 
            
        ans = 0
        for i in range(n):
            cur = i
            total = i
            for p in kb:
                total += stsum[cur][p]
                cur = stjump[cur][p]
            ans = max(ans,total)
        return ans