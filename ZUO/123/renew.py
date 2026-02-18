r
    if not input_data: return

    n = int(input_data[0])
    h = n//2
    g = [[] for _ in range(n + 1)]
    idx = 1
    for _ in range(n - 1):
        u, v = int(input_data[idx]), int(input_data[idx + 1])
        g[u].append(v)
        g[v].append(u)
        idx += 2
    
    size = [0] * (n + 1)
    maxsub = [0] * (n + 1)
    inner1 = [0] * (n + 1)
    inner2 = [0] * (n + 1)
    choose = [0] * (n + 1)
    outer = [0] * (n + 1)

    def dfs1(u,f):
        size[u] = 1
        for v in g[u]:
            if v==f:continue

            dfs1(v,u)
            size[u]+=size[v]

            #维护最大儿子
            if size[v]>maxsub[u]:
                maxsub[u] = v
            
            # 计算该分支内符合要求的最大子树（要么直接是v，
            # 要么是v内部符合要求的最大值）
            inner_size = size[v] if size[v]<=h else inner1[v]

            #更新inner1 和 inner2
            if inner_size > inner1[u]:
                inner2[u] = inner1[u]
                inner1[u] = inner_size
                choose[u] = v
            elif inner_size > inner2[u]:
                inner2[u] = inner_size
        
        def dfs2(u,f):
            for v in g[u]:
                if v==f:continue

                # 计算 v 外部方向的最大合法子树
                # 情况1：向上看，剔除掉v分支后，剩下的树
                # 大小 <= n/2，则剩下的树直接是一个合法的子树
                if n - size[v] <=h:
                    outer[u] = n - size[v]
                else:
                    # 情况2：剩下的树太大，只能利用父节点方向已有的合法子树
                    # 如果 v 是 u 的 inner1 来源，则只能用 inner2
                    if choose[u] == v:
                        outer[u] = max(outer[u],inner2[u])
                    else:
                        outer[u] = max(outer[u],inner1[u])
                
                dfs2(v,u)
            

            dfs1(1,0)
            dfs2(1,0)

            res = []
            for u in range(1,n+1):
                f = True

                # 1. 检查内部最大分支
                if size[maxsub[u]] > h:
                    if size[maxsub[u]] - inner1[maxsub[u]] > h:
                        f = False
                
                elif n - size[u] > h:
                    if n - size[u] - outer[u] > h:
                        f = False
                
                res.append("1" if f else "0")
            
            sys.stdout.write(" ".join(res)+"\n")

if __name__ == "__main__":
    solve()

renew