import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return

    prt = 0
    tc = int(input_data[prt])
    prt += 1

    for _ in range(tc):
        n = int(input_data[prt])
        ptr+=1

        g = [[] for _ in range(n + 1)]
        deg = [0] * (n + 1)

        for _ in range(n-1):
            u = int(input_data[ptr])
            v = int(input_data[ptr+1])
            w = int(input_data[ptr+2])

            g[u].append((v, w))
            deg[u] += 1
            g[v].append((u, w))
            deg[v] += 1
            ptr += 3
        
        flow = [0]*(n+1)
        dp = [0]*(n+1)

        def dfs1(u,f):
            for v,w in g[u]:
                if v!=f:
                    dfs1(v,u)
                    if deg[v]==1:
                        flow[u] += w
                    else:
                        flow[u] += min(flow[v],w)
        
        def dfs2(u,f):
            for v,w in g[u]:
                if v!=f:
                    if deg[v]==1:
                        dp[v] = flow[u] + w
                    else:
                        u_out = dp[u] - min(flow[v],w)
                        dp[v] = flow[v] + min(w,u_out)
                    dfs2(v,u)
        
    if n==1:
        sys.stdout.write("0\n")
        continue
    dfs1(1,0)
    dp[1] = flow[1]
    dfs2(1,0)
    sys.stdout.write(str(max(dp[1:]))+"\n")

if __name__ == "__main__":
    solve()