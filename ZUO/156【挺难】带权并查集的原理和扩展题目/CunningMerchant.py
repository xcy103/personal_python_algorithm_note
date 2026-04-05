#  狡猾的商人，带权并查集模版题2
#  有n个月的收入，下标1 ~ n，但是并不知道每个月收入是多少
#  操作 l r v，代表从第l个月到第r个月，总收入为v
#  一共给你m个操作，请判断给定的数据是自洽还是自相矛盾
#  自洽打印true，自相矛盾打印false
#  1 <= n <= 100    1 <= m <= 1000
#  总收入不会超过int类型范围
#  测试链接 : https://www.luogu.com.cn/problem/P2294

# 这个是推矛盾
# 这道题提到了，如果一次测试只有一组测试，不需要清空
# 如果有多组需要清空

import sys
input = sys.stdin.readline

MAXN = 105

father = [0] * MAXN
dist = [0] * MAXN

def prepare(n):
    for i in range(n + 1):
        father[i] = i
        dist[i] = 0

def find(x):
    if father[x] != x:
        root = find(father[x])
        dist[x] += dist[father[x]]
        father[x] = root
    return father[x]

def union(l, r, v):
    lf = find(l)
    rf = find(r)
    if lf != rf:
        father[lf] = rf
        # 我们合并的时候，是dist[r] - dist[l]
        # 这里的合并刚开始没看懂，因为路径压缩之后，这个lf就是
        # 这个连通块的代表元素，我疑惑的点是为什么不是lf和rf
        # 因为肯定是代表元素，连挺块里元素的距离，都是以代表元素
        # 为参照，现在合并了，要改写的代表元素的距离
        # 要通过l,r的关系得出
        dist[lf] = v + dist[r] - dist[l]

def check(l, r, v):
    if find(l) == find(r):
        # 取得距离的时候是dist[l] - dist[r]
        if dist[l] - dist[r] != v:
            return False
    return True


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    n += 1  # 和Java一致（前缀和技巧）

    prepare(n)

    ans = True

    for _ in range(m):
        l, r, v = map(int, input().split())
        r += 1

        if not check(l, r, v):
            ans = False
        else:
            union(l, r, v)

    print("true" if ans else "false")