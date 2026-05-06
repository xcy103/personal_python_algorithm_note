class Solution:
    def countDigitOne(self, k: int) -> int:
        s = list(map(int,str(k)))

        n = len(s)
        pre = [1]*(n+1)
        for i in range(1,n+1):
            pre[i] = pre[i-1]*(s[i-1]+1)
        
        suf = [1]*(n+1)
        for i in range(n-1,-1,-1):
            suf[i] = suf[i+1]*(s[i]+1)
        
        ans = 0
        x = 0
        y = k
        for i in range(n):
            if s[i]==1:
                #取不到上限制
                ans+=y-s[i]*pow(10,n-i-1)+1
                if x>0:
                    ans+=x*pow(10,n-i-1)
            elif s[i]==0:
                ans+=x*pow(10,n-i-1)
            else:
                ans+=(x+1)*pow(10,n-i-1)
            x = x*10+s[i]
            y-=s[i]*pow(10,n-i-1)
        return ans

                    