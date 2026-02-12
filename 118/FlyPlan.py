# 国旗计划
# 给定点的数量m，点的编号1~m，所有点围成一个环
# i号点一定顺时针到达i+1号点，最终m号点顺指针回到1号点
# 给定n条线段，每条线段(a, b)，表示线段从点a顺时针到点b
# 输入数据保证所有线段可以把整个环覆盖
# 输入数据保证每条线段不会完全在另一条线段的内部
# 也就是线段之间可能有重合但一定互不包含
# 返回一个长度为n的结果数组ans，ans[x]表示一定选x号线段的情况下
# 至少选几条线段能覆盖整个环
# 测试链接 : https://www.luogu.com.cn/problem/P4155


MAXM = 2000001
LIMIT = 18

line = [[0,0,0] for _ in range((MAXM<<1)+1)]
stjump = [[0]*LIMIT for _ in range((MAXM<<1)+1)]
ans = [0]*(MAXM)

n = 0
m = 0
power = 0
def log2(n):
    ans =0 
    while (1<<ans)<=n>>1:
        ans+=1
    return ans

def build():
    global line,stjump
    
    for i in range(1,n+1):
        if line[i][1] > line[i][2]:
            line[i][2]+=m
    
    line[1:n+1] = sorted(line[1:n+1],key=lambda x:x[1])

    for i in range(1,n+1):
        line[i+n][0] = line[i][0]
        line[i+n][1] = line[i][1]+m
        line[i+n][2] = line[i][2]+m
    
    e = n<<1

    arrive = 1

    for i in range(1,e+1):
        while arrive+1<=e and line[arrive+1][1]<=line[i][2]:
            arrive+=1
        stjump[i][0] = arrive
    
    for p in range(1,power+1):
        for i in range(1,e+1):
            stjump[i][p] = stjump[stjump[i][p-1]][p-1]
    
def jump(i):
    aim = line[i][1]+m
    cur = i
    cnt = 0
    for p in range(power,-1,-1):
        nxt = stjump[cur][p]
        if nxt!=0 and line[nxt][2] < aim:
            cnt+= 1<<p
            cur = nxt
    return cnt+2

def solve():
    global power
    power = log2(n)
    build()
    for i in range(1,n+1):
        ans[line[i][0]] = jump(i)