#  聚会后送每个人回家最短用时
#  给定一棵n个点的树，边权代表走过边需要花费的时间
#  给定k个人分别在树上的哪些节点
#  这k个人选择了一个聚会点，所有的人都去往聚会点进行聚会
#  聚会结束后，所有人都会上一辆车，车会把每个人送回家
#  送完最后一个乘客，车不需要回到聚会点
#  如果聚会点在i，请问从聚会地点出发直到送最后一个人回家，最短用时多少
#  i = 1 ~ n，打印所有的答案
#  测试链接 : https://www.luogu.com.cn/problem/P6419

import sys

def solve()
    
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iter0 = iter(input_data)
    try:
        n = int(next(iter0))
        k = int(next(iter0))
    except StopIteration:
        return
    
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u = int(next(iter0))
        v = int(next(iter0))
        w = int(next(iter0))
        g[u].append((v, w))
        g[v].append((u, w))
    
    people = [0] * (n + 1)   # 子树内有多少乘客
    incost = [0] * (n + 1)   # 子树内送完并回来的代价
    inner1 = [0] * (n + 1)   # 子树内最长链
    inner2 = [0] * (n + 1)   # 子树内次长链
    choose = [0] * (n + 1)   # 最长链来自于哪个子节点
    outcost = [0] * (n + 1)  # 子树外送完并回来的代价
    outer = [0] * (n + 1)    # 子树外最长链

    for _ in range(k):
        people[int(next(iter0))] += 1

    # 第一次 DFS：处理子树内部信息 (incost, inner1, inner2, choose)
    def dfs1(u, f):
        for v, w in g[u]:
            if v==f:
                continue

            people[u] += people[v]

            if people[v]>0:
                incost[u] += incost[v] + w*2

                dist = inner1[v] + w
                if dist>inner1[u]:
                    inner2[u] = inner1[u]
                    inner1[u] = dist
                    choose[u] = v
                elif dist>inner2[u]:
                    inner2[u] = dist
    
    def dfs2(u, f):
        for v, w in g[u]:
            if v==f:
                continue
            
            if k - people[v]>0:

                if people[v] ==0:
                    outcost[v] = outcost[u] + incost[u] + w*2
                else:
                    outcost[v] =  outcost[u] + incost[u] - incost[v]

                # 计算 outer
                # 如果u的最长链不经过v，则v往上的最长链可以是 
                # (u往上的最长链) 或 (u子树内的最长链)
                if v != choose[u]:
                    outer[v] = max(outer[u], inner1[u]) + w
                else:
                    outer[v] = max(outer[u], inner2[v]) + w
            dfs2(v, u)
        
        dfs1(1,0)
        dfs2(1,0)

        output = []
        for i in range(1,n+1):
            # 答案 = 总回路代价 - 不需要走回头的最长路径
            # 总回路代价 = 子树内回路 + 子树外回路
            # 最长路径 = max(子树内最长, 子树外最长)
            ans = incost[i] + outcost[i] - max(inner1[i], outer[i])
            output.append(str(ans))
        
        sys.stdout.write('\n'.join(output) + '\n')

if __name__ == '__main__':
    solve()
