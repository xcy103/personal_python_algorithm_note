import sys
input = sys.stdin.readline

t = int(input())
res = []

for _ in range(t):
    n = int(input())
    if n == 1:
        res.append("1")
        continue

    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

    size = [0] * n
    ans = 0

    # (u, fa, state)
    # state = 0 -> 进入节点
    # state = 1 -> 子节点处理完，回溯
    stack = [(0, -1, 0)]

    while stack:
        u, fa, state = stack.pop()

        if state == 0:
            # 第一次到达，压回溯标记
            stack.append((u, fa, 1))
            for v in g[u]:
                if v == fa:
                    continue
                stack.append((v, u, 0))

        else:
            # 回溯阶段（子树已经算完）
            t_size = 1
            tag = True

            for v in g[u]:
                if v == fa:
                    continue
                nums = size[v]
                tag &= (nums % 2) == 1
                t_size += nums

            if n - t_size > 0:
                tag &= ((n - t_size) % 2) == 1

            if tag:
                ans += 1

            size[u] = t_size

    res.append(str(ans))

print('\n'.join(res))