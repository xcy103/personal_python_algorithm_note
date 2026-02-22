#  消防(递归版)
#  一共n个节点，编号1~n，有n-1条边连接成一棵树，每条边上有非负权值
#  给定一个非负整数s，表示可以在树上选择一条长度不超过s的路径
#  然后在这条路径的点上建立消防站，每个居民可以去往这条路径上的任何消防站
#  目标：哪怕最远的居民走到消防站的距离也要尽量少
#  返回最远居民走到消防站的最短距离
#  测试链接 : https://www.luogu.com.cn/problem/P2491
# 思路就是，在直径上建立消防站
# 然后开始树上直径滑窗，比较滑窗内的点到start，滑窗内的点到end
# 滑窗内的点maxDist这三者的最大值，和之前的值取最小
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, s = map(int, input().split())

# 邻接表
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

dist = [0] * (n + 1)
last = [0] * (n + 1)
pred = [0] * (n + 1)
diameter_path = [False]*(n+1)
maxDist = [0]*(n+1)
diameter = 0

def dfs(u,f):
    for v,w in graph[u]:
        if v != f:
            dist[v] = dist[u] + w
            last[v] = u
            pred[v] = w
            dfs(v, u)

def find_diameter():
    dfs(1,0)
    start = 1
    for i in range(2,n+1):
        if dist[i] > dist[start]:
            start = i
    
    dist = [0]*(n+1)
    dfs(start,0)
    end = 1
    for i in range(2, n + 1):
        if dist[i] > dist[end]:
            end = i
    return start,end,dist[end]

def max_distance_except_diameter(u,f):
    ans = 0
    for v,w in graph[u]:
        if v!=f and not diameter_path[v]:
            ans = max(ans, max_distance_except_diameter(v,u) + w)
    
    return ans

def prepare_distance(end):
    global start
    cur = end
    while cur!= 0:
        diameter_path[cur] = True
        cur = last[cur]
    
    cur = end
    while cur != 0:
        maxDist[cur] = max_distance_except_diameter(cur,0)
        cur = last[cur]

def compute():
    global start, end, s, diameter
    queue = [0]*(n+1)
    h = t =0
    suml = sumr = 0
    ans = float('inf')

    l = r = end

    while r!=0:
        while r!=0 and sumr - suml + pred[r] <= s:
            while h<t and maxDist[queue[t-1]]<=maxDist[r]: t -= 1
        
            sumr+=pred[r]
            queue[t] = r
            t+=1
            r = last[r]
        ans = min(ans, max(suml,diameter - sumr,maxDist[queue[h]]))

        if queue[h] == l:
            h+=1
        suml += pred[l]
        l = last[l]

start, end, diameter = find_diameter()
prepare_distance(end)

print()