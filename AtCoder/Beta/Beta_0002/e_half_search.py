#折半搜索

import sys
import bisect

def solve():
    # 使用 fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    s = int(input_data[1])
    candy = list(map(int, input_data[2:]))

    # 1. 分成两半
    mid = n // 2
    c1 = candy[:mid]
    c2 = candy[mid:]

    # 2. 生成子集和的函数（优化：不重复计算 sum）
    def get_sums(arr):
        res = [0]
        for x in arr:
            # 对于数组中的每个数，现有的每个和都可以选或不选这个数
            res += [curr + x for curr in res]
        return res

    a1 = get_sums(c1)
    a2 = get_sums(c2)

    # 3. 排序其中一个，进行二分查找
    a1.sort()
    
    op = 0
    for x in a2:
        target = s - x
        # 4. 修正：直接 r - l 即可得到数量
        l = bisect.bisect_left(a1, target)
        r = bisect.bisect_right(a1, target)
        op += (r - l)

    print(op)

solve()