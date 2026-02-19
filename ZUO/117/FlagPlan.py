import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    ptr = 0
    m,n = int(data[ptr]),int(data[ptr+1])
    ptr+=2

    lines = []
    for i in range(1,n+1):
        l,r = int(data[ptr]),int(data[ptr+1])
        ptr+=2
        if l>r:
            r+=m
        lines.append((l,r,i))
    
    lines.sort()
    for i in range(n):
        lines.append((lines[i][0]+m,lines[i][1]+m,lines[i][2]))
    
    total_lines = 2*n
    limit = 18

    stjump = [[0]*limit for _ in range(total_lines)]
    arrive = 0
    for i in range(total_lines):
        while arrive+1<total_lines and lines[arrive+1][0]<lines[i][1]:
            arrive+=1
        stjump[i][0] = arrive
    
    power = n.bit_length()-1
    for p in range(1,power+1):
        for i in range(total_lines):
            stjump[i][p] = stjump[stjump[i][p-1]][p-1]
    
    ans = [0]*(n+1)

    for i in range(n):
        aim = lines[i][0]+m
        cur = i
        cnt = 0
        for p in range(power,-1,-1):
            if lines[stjump[cur][p]][0]<aim:
                cur = stjump[cur][p]
                cnt+=1<<p
        ans[lines[i][2]] = cnt+2