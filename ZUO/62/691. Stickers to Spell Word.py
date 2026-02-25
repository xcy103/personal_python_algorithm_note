#思路就是，单词字母顺序可以随便改
#先创建一个图，每一个单词可以搞定什么字母，
#然后开始bfs，开始的单词作为起始点
#然后选每个单词看看能消除什么字母，检出什么单词
#这些单词作为下一层，下一次迭代的时候就从他们开始
#直到最先遇到空元素，就是终点次数
from collections import defaultdict
from collections import deque
from typing import List
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        g = defaultdict(list)

        for s in stickers:
            s = ''.join(sorted(s))
            used = set()
            for ch in s:
                if ch not in used:
                    g[ch].append(s)
                    used.add(ch)
        target = ''.join(sorted(list(target)))

        q = deque([target])
        vis = {target}
        l = 1
        while q:
            for _ in range(len(q)):
                cur = q.popleft()

                for s in g[cur[0]]:
                    nxt = self.subtract(cur,s)
                    if nxt=="":return l

                    if nxt not in vis:
                        vis.add(nxt)
                        q.append(nxt)
            l+=1
        
        return -1
    
    def subtract(self,t,s):
        i = j = 0
        res = []
        while i<len(t):
            if j==len(s):
                res.append(t[i])
                i+=1
            else:
                if t[i]<s[j]:
                    res.append(t[i])
                    i+=1
                elif t[i]>s[j]:
                    j+=1
                else:
                    i+=1
                    j+=1
        return ''.join(res)