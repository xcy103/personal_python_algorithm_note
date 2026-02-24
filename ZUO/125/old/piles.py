# 比较难分析的是，如何进行状态转移，
# 如何设置参数，每一个参数的意义是什么
# 这里的s的一位表示这一列有没有放置竖的瓷砖，
import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return

    idx = 0
    while idx < len(data):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx+=2

        if n==0 and m==0: break

        if n<m:
            n,m = m,n

        def get(s,j):
            return (s>>j)&1
        def set(s,j,v):
            if v==0: return s&(~(1<<j))
            else: return s|(1<<j)
        
        @cache
        def f(i,j,s):
            if i==n:
                return 1
            if j==m:
                return f(i+1,0,s)

            ans = 0
            if get(s,j)==1:
                ans += f(i,j+1,set(s,j,0))
            else:
                if i+1<n:
                    ans+=f(i,j+1,set(s,j,1))
                if j+1<m and get(s,j+1)==0:
                    ans+=f(i,j+2,s)
            return ans

        if (m*n)%2!=0:
            print(0)
        else:
            print(f(0,0,0))

if __name__=='__main__':
    solve()