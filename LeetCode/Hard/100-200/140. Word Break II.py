class Solution:
    def wordBreak(self, s: str, w: List[str]) -> List[str]:
        
        ans = []
        path = []
        n = len(s)
        def dfs(i):
            if i==n:
                ans.append(" ".join(path))
                return
            
            for j in range(i,n):
                t = s[i:j+1]
                if t in w:
                    path.append(t)
                    dfs(j+1)
                    path.pop()
        dfs(0)
        return ans