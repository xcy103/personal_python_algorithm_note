# 如果有 $m$ 个离散的 $y$ 坐标点，它们之间只有 $m-1$ 个基本区间。
import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    lines = []
    y_coords = []
    ptr = 1
    for i in range(n):
        x1, y1, x2, y2 = map(int, data[ptr:ptr+4])
        ptr += 4
        lines.append((x1, y1, y2, 1))  # 开始
        lines.append((x2, y1, y2, -1)) # 结束
        y_coords.append(y1)
        y_coords.append(y2)
    
    # 离散化
    y_coords = sorted(set(y_coords))
    m = len(y_coords)
    rank = {v: i+1 for i, v in enumerate(y_coords)}

    cnt = [0]*(m<<2)
    cover = [0]*(m<<2)

    def up(i, l, r):
        if cnt[i]>0:
            cover[i] = y_coords[r] - y_coords[l-1]
        elif l==r:
            cover[i] = 0
        else:
            cover[i] = cover[i<<1] + cover[i<<1|1]
    
    def modify(jobl, jobr, val, l, r, i):
        if jobl<=l and jobr>=r:
            cnt[i] += val
        else:
            mid = (l+r)>>1
            if jobl<=mid:
                modify(jobl, jobr, val, l, mid, i<<1)
            if jobr>mid:
                modify(jobl, jobr, val, mid+1, r, i<<1|1)
        up(i,l,r)
    
    lines.sort()
    ans = 0
    pre = lines[0][0]
    for x, y1, y2, typ in lines:
        ans += cover[1]*(x-pre)
        pre = x
        L = rank[y1]
        R = rank[y2]-1
        if L<=R:
            # 不可以这么传递，因为我们搜索出来的索引，是点的
            # 排名，但是我们不是在找点，我们是在找区间。
            # 所以我们要给区间右边界的点的排名-1
            #modify(L, R, typ, 1, m-1, 1)
            modify(L, R, typ, 1, m-1, 1)
    print(ans)

if __name__ == "__main__":
    solve()