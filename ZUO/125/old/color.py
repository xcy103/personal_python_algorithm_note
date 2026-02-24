# 如果k==2直接就是交替

import sys

def solve():

    data = sys.stdin.read().split()
    if not data: return

    n = int(data[0])
    m = int(data[1])
    k = int(data[2])

    MOD = 376544743

    start = [int(x) for x in data[3:3+m]]
    end = [int(x) for x in data[3+m:3+2*m]]

    if k==2:
        p = True
        for i in range(m):
            if i>0 and start[i]==start[i-1]:
                p = False
            if i>0 and end[i]==end[i-1]:
                p = False
            if n%2==0:
                if start[i]==end[i]:
                    p = False
            else:
                if start[i]!=end[i]:
                    p = False
        print(1 if possible else 0)
        return

    def get_color(s,j):
        return (s>>(j<<1))&3
    
    def set_color(s,j,v):
        return (s&~(3<<(j<<1)))|(v<<(j<<1))

    start_status = 0
    for j in range(m):
        start_status = set_color(start_status, j, start[j])

    end_status = 0
    for j in range(m):
        end_status |= (end[j] << (j << 1))
    
    @__cached__
    def f(i,j,s):
        if i==n-1:
            for idx in range(m):
                if get_color(s,idx)==\
                get_color(end_status,idx):
                    return 0
            return 1
        if j==m:
            return f(i+1,0,s)

        ans = 0
        up = get_color(s,j)
        left = get_color(s,j-1) if j>0 else -1

        for c in range(k):
            if c!=up and c!=left:
                ans = (ans+f(i,j+1,set_color(s,j,c)))%MOD
        
        return ans
    print(f(1,0,start_status))

if __name__=='__main__':
    solve()