#难在收集路径，思路还是从开始词拓展
#逐位替换，生成新的词，这些新的词组成下一层，生成新的词同时我们记录新的词可以返回到的老词
#如果这一层有结束词，先等这一层生成完毕，然后再结束
#然后就是dfs，从结束词开始，我们记录了那些词可以变为结束词
#我们就逐个从这些词往回递归，同时加入path
from collections import defaultdict
from typing import List
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        g = defaultdict(list)
        cur = {beginWord}
        f = False

        while cur and not f:
            wordSet-=cur
            nxt = set()
            for w in cur:
                s = list(w)
                for i,old in enumerate(s):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        s[i] = c
                        nw = ''.join(s)
                        if nw in wordSet:
                            if nw==endWord:
                                f = True
                            g[nw].append(w)
                            nxt.add(nw)
                    s[i] = old
            cur = nxt
        
        res = []
        def dfs(word,path):
            if word==beginWord:
                res.append(path[::-1])
                return 
            for pre in g[word]:
                dfs(pre,path+[pre])
        
        if f:
            dfs(endWord,[endWord])
        
        return res