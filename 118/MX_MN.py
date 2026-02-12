# ST表查询最大值和最小值
# 给定一个长度为n的数组arr，一共有m次查询
# 每次查询arr[l~r]上的最大值和最小值
# 每次查询只需要打印最大值-最小值的结果
# 测试链接 : https://www.luogu.com.cn/problem/P2880


MAXN = 50001
LIMIT = 16

arr = [0]*MAXN
log2 = [0]*MAXN
stmax = [[0]*LIMIT for _ in range(MAXN)]
stmin = [[0]*LIMIT for _ in range(MAXN)]

def build(n):
    log2[0] = -1
    for i in range(1,n+1):
        log2[i] = log2[i>>1]+1
        stmax[i][0] = arr[i]
        stmin[i][0] = arr[i]
    
    for p in range(1,log2[n]+1):
        l = 1<<p
        h = 1<<(p-1)
        for i in range(1,n-l+2):
            stmax[i][p] = max(stmax[i][p-1],stmax[i+h][p-1])
            stmin[i][p] = min(stmin[i][p-1],stmin[i+h][p-1])


def query(l,r):
    p = log2[r-l+1]
    a = max(stmax[l][p],stmax[r-(1<<p)+1][p])
    b = min(stmin[l][p],stmin[r-(1<<p)+1][p])
    return a-b