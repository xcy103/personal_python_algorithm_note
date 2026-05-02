class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        l = 0
        r = 0

        ans = inf
        g = ""
        c = Counter(t)
        k = Counter()
        need = len(t)
        while r<n:
            if k[s[r]]<c[s[r]]:
                need-=1
            k[s[r]]+=1

            while need==0:
                if r-l+1<ans:
                    g = s[l:r+1]
                    ans = r-l+1
                
                k[s[l]]-=1
                if k[s[l]]<c[s[l]]:
                    need+=1
                l+=1
            r+=1
        return g