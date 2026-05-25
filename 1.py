from math import inf
def countSubgraphsForEachDiameter(n: int, edges):
    bit = 1 << n
    res = [0] * n

    def f(mask):
        g = [[inf] * n for _ in range(n)]
        for a, b in edges:
            a -= 1
            b -= 1
            if (mask & (1 << a)) and (mask & (1 << b)):
                g[a][b] = 1
                g[b][a] = 1

        idx = []
        for i in range(n):
            if mask & (1 << i):
                g[i][i] = 0
                idx.append(i)

        # floyd
        for k in idx:
            for a in idx:
                for b in idx:
                    g[a][b] = min(g[a][k] + g[k][b], g[a][b])

        d = -1
        num = 0
        for a in idx:
            for b in idx:
                if a==b:continue
                if g[a][b] == inf:
                    return inf, 0
                if g[a][b] > d:
                    d = g[a][b]
                    num = 1
                elif g[a][b] == d:
                    num += 1

        return d, num//2
    for mask in range(1,bit):
        if (mask&(mask-1))==0:continue
        #找到子集了，开始dij
        d,num = f(mask)
        if d==inf:continue
        res[d] += num
    print(res)
countSubgraphsForEachDiameter(4,[[1,2],[2,3],[2,4]])