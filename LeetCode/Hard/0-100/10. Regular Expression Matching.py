class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        s = list(s)
        p = list(p)

        @cache
        def f(i,j):
            if i==len(s):
                if j==len(p):
                    return True
                #p没到头，但是s到头了，所以要求p后面都是*
                return (j+1<len(p)) and p[j+1]=='*' and f(i,j+2)
            if j==len(p):
                return False
            
            #先判断后面不是*的情况
            if j+1==len(p) or p[j+1]!='*':
                if s[i]==p[j] or p[j]=='.':
                    return f(i+1,j+1)
                else:
                    return False
            
            p1 = f(i,j+2)
            #j+1一定是'*'
            p2 = False
            if s[i]==p[j] or p[j]=='.':
                p2 = f(i+1,j)
            
            return p1 or p2
        return f(0,0)
    