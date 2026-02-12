#  翻转道路数量最少的首都
#  给定一棵n个点的树，但是给定的每条边都是有向的
#  需要选择某个城市为首都，要求首都一定可以去往任何一个城市
#  这样一来，可能需要翻转一些边的方向才能做到，现在想翻转道路的数量尽量少
#  打印最少翻转几条道路就可以拥有首都
#  如果有若干点做首都时，翻转道路的数量都是最少的，那么打印这些点
#  测试链接 : https://www.luogu.com.cn/problem/CF219D

import sys

def solve():
  
    input_data = sys.stdin.read().split()
    if not input_data: return
    ptr = 0
    while ptr < len(input_data):
        n = int(input_data[ptr])
        ptr += 1

        g = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u, v = map(int, input_data[ptr:ptr + 2])
            ptr += 2
            g[u].append((v, 0))
            g[v].append((u, 1))
        
        re = [0]*(n+1)
        dp = [0]*(n+1)

        def dfs1(u,f):
            for v,w in g[u]:
                if v!=f:
                    dfs1(v,u)
                    re[u] += re[v] + w
            
        def dfs2(u,f):
            for v,w in g[u]:
                if v!=f:
                    if w==0:
                        dp[v] = dp[u] + 1
                    else:
                        dp[v] = dp[u] - 1
        
        dfs1(1,0)
        dp[1] = re[1]
        dfs2(1,0)
        min_val = min(dp[1:])
        ans_node = [str(i) for i in range(1,n+1) if dp[i]==min_val]
        sys.stdout.write(f"{min_val}\n")
        sys.stdout.write(" ".join(ans_node)+"\n")

if __name__ == "__main__":
    solve()

        