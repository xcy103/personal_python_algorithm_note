import sys

# 1. 必须提高递归深度限制
sys.setrecursionlimit(20000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    
    rects = []
    ptr = 1
    for _ in range(n):
        x1, y1, x2, y2 = map(int, data[ptr:ptr+4])
        ptr += 4
        rects.append((x1, x2, y1, y2))
    
    # 将 scan 定义在外部，但把线段树操作放进去
    def scan(lines, coords):
        coords = sorted(set(coords))
        m = len(coords)
        rank = {y: i + 1 for i, y in enumerate(coords)}

        # 2. 线段树数组必须在这里定义，或者用 nonlocal
        # 否则 add 和 up 函数引用的 y_coords 会出错
        tree_times = [0] * (m << 2)
        tree_cover = [0] * (m << 2)

        def up(i, l, r):
            if tree_times[i] > 0:
                tree_cover[i] = coords[r] - coords[l-1]
            else:
                # 如果是叶子节点，tree_cover[i << 1] 永远是 0，结果正确
                # 如果是非叶子节点，正常合并子节点
                tree_cover[i] = tree_cover[i << 1] + tree_cover[i << 1 | 1] if l < r else 0

        def add(jobl, jobr, val, l, r, i):
            if jobl <= l and jobr >= r:
                tree_times[i] += val
            else:
                mid = (l + r) >> 1
                if jobl <= mid:
                    add(jobl, jobr, val, l, mid, i << 1)
                if jobr > mid:
                    add(jobl, jobr, val, mid + 1, r, i << 1 | 1)
            up(i, l, r)

        lines.sort(key=lambda x: (x[0], -x[3]))
        res = 0
        pre = 0
        for _, v1, v2, val in lines:
            L = rank[v1]
            R = rank[v2] - 1
            if L <= R:
                add(L, R, val, 1, m - 1, 1)
            res += abs(tree_cover[1] - pre)
            pre = tree_cover[1]
        return res

    # 垂直边扫描
    vlines = []
    v_coords = []
    for x1, x2, y1, y2 in rects:
        vlines.append((x1, y1, y2, 1))
        vlines.append((x2, y1, y2, -1))
        v_coords.append(y1)
        v_coords.append(y2)
    ans = scan(vlines, v_coords)

    # 水平边扫描
    hlines = []
    h_coords = []
    for x1, x2, y1, y2 in rects:
        hlines.append((y1, x1, x2, 1))
        hlines.append((y2, x1, x2, -1))
        h_coords.append(x1)
        h_coords.append(x2)
    ans += scan(hlines, h_coords)
    
    sys.stdout.write(str(ans) + '\n')

if __name__ == "__main__":
    solve()