# 多加一个leftup

import sys

def solve():

    data = sys.stdin.read().split()
    if not data: return
    n = int(data[0])
    kings = int(data[1])

    @__cached__
    def f(i, j, s,leftup,k):
        if i==n:
            return 1 if k==0 else 0
        if j==n:
            return f(i+1,0,s,0,k)
        
        left = 0 if j==0 else (s>>(j-1))&1
        up = (s>>j)&1
        rightup = 0 if j==n-1 else (s>>(j+1))&1

        ans = f(i,j+1,s&(~(1<<j)),up,k)
        if (k>0 and left==0 and up==0 and rightup==0 and leftup==0):
            ans += f(i,j+1,s|(1<<j),up,k-1)
        
        return ans
    return f(0,0,0,0,kings)

if __name__ == '__main__':
    solve()
