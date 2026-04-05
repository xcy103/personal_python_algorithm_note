# 一维数轴模型


#  推导部分和，带权并查集模版题1
#  有n个数字，下标1 ~ n，但是并不知道每个数字是多少
#  先给出m个数字段的累加和，再查询q个数字段的累加和
#  给出数字段累加和的操作 l r v，代表l~r范围上的数字，累加和为v
#  查询数字段累加和的操作 l r，代表查询l~r范围上的数字累加和
#  请根据m个给定，完成q个查询，如果某个查询无法给出答案，打印"UNKNOWN"
#  1 <= n, m, q <= 10^5
#  累加和不会超过long类型范围
#  测试链接 : https://www.luogu.com.cn/problem/P8779
import sys

sys.setrecursionlimit(60000)

INF = float('inf')

# 读取输入
n, m, q = map(int, input().split())
n += 1  # 和Java一样

f = list(range(n+1))
dist = [0]*(n+1)

def find(x):
    if f[x]!=x:
        old = f[x]
        f[x] = find(old)
        dist[x]+=dist[old]
    return f[x]

def unite(l,r,v):
    lf = find(l)
    rf = find(r)
    if lf!=rf:
        f[lf] = rf
        dist[lf] = v+dist[r]-dist[l]

def query(l,r):
    if find(l)!=find(r):
        return INF
    return dist[l] - dist[r]

#处理约束
for _ in range(m):
    l,r,v =  map(int, input().split())
    r+=1
    unite(l,r,v)

for _ in range(q):
    l, r = map(int, input().split())
    r += 1
    ans = query(l, r)
    if ans == INF:
        print("UNKNOWN")
    else:
        print(ans)