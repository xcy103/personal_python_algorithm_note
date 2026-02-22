#  巡逻
#  一共n个节点，编号1~n，结构是一棵树，每条边都是双向的
#  警察局在1号点，警车每天从1号点出发，一定要走过树上所有的边，最后回到1号点
#  现在为了减少经过边的数量，你可以新建k条边，把树上任意两点直接相连
#  并且每天警车必须经过新建的道路正好一次
#  计算出最佳的新建道路的方案，返回巡逻走边数量的最小值
#  测试链接 : https://www.luogu.com.cn/problem/P3629
#  只有三种情况，第一是k==1，那么就直接在直径两端连线即可
#  第二种情况是k==2，我们许要找出最长直径和次长直径
#  1.两条直径公共的部分只有一点，这个好分析
#  2.两条直径有公共线段部分，这些线段走了两次，要加上
#  但是我们可以把最长直径上的边权都改为-1，当我们求出次长直径时候
#  就可以获得这两个部分的代价了
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, k = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dist = [0]*(n+1)
last = [0]*(n+1)
diameter_path = [0]*(n+1)

def dfs(u,f):
    for v in graph[u]:
        if v == f:
            continue
        dist[v] = dist[u] + 1
        last[v] = u
        dfs(v, u)

def find_diameter(u,f):
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

diameter2 = 0

def dp(u,f):
    global diameter2
    for v in graph[u]:
        if v == f:
            continue
        dp(v,u)
    for v in graph[u]:
        if v==f:
            continue
        w = -1 if diameter_path[v] and diameter_path[u] else 1
        diameter2 = max(diameter2, dist[u] + dist[v] + w)
        dist[u] = max(dist[u], dist[v] + w)

def compute():
    global diameter2

    start, end, diameter1 = find_diameter()

    if k==1:
        return 2*(n-1) - diameter1 + 1

    cur = end
    while cur != start:
        diameter_path[cur] = True
        cur = last[cur]
    
    dist = [0]*(n+1)
    diameter2 = 0
    dp(1,0)
    return 2 * (n - 1) - diameter1 - diameter2 + 2

print(compute())