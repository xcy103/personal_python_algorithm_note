# 这道题又用到了next数组，
# 这个next数组的含义是，从当前出发，
# 找到下一个字符需要长度

class Solution:
    def getMaxRepetitions(self, s1: str, a: int, s2: str, b: int) -> int:
        n = len(s1)
        s1 = list(s1)
        s2 = list(s2)

        nxt = [[-1]*26 for _ in range(n)]

        right = [-1]*26

        for i in range(n-1,-1,-1):
            right[ord(s1[i]) - ord('a')] = i+n
        
        for i in range(n-1,-1,-1):
            right[ord(s1[i]) - ord('a')] = i
            for j in range(26):
                if right[j]!=-1:
                    nxt[i][j] = right[j]-i+1
                else:
                    nxt[i][j] = -1
        
        for c in s2:
            if nxt[0][ord(c)-ord('a')]==-1:
                return 0
        
        stjump = [[0]*30 for _ in range(n)]

        for i in range(n):
            cur = i
            l = 0
            for c in s2:
                step = nxt[cur][ord(c) - ord('a')]
                l+=step
                cur = (cur+step)%n
            stjump[i][0] = l
        
        for p in range(1,30):
            for i in range(n):
                pre = stjump[i][p-1]
                nxt_pos = (i+pre)%n
                stjump[i][p] = pre + stjump[nxt_pos][p-1]
        
        total = n*a
        ans = 0
        start = 0
        for p in range(29,-1,-1):
            if start + stjump[start%n][p]<=total:
                ans+=(1<<p)
                start += stjump[start%n][p]
        return ans//b