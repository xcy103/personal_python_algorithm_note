# ST表的优势和劣势
# RMQ问题(Range Maximum/Minimum Query)可以用ST表维护，也可以用线段树等结构维护
# ST表的优势:构建过程时间复杂度0(n*logn)，单次查询时间复杂度0(1)，代码量较小
# ST表的劣势:需要空间较大，能维护的信息非常有限，不支持修改操作
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    n = int(input_data[ptr])
    ptr += 1
    m = int(input_data[ptr])
    ptr += 1
    
    # MAXN 为 50001, LIMIT 为 16 (2^15 <= 50001)
    # Python 数组下标从 0 开始更方便，为了对应 Java 代码，我们开 N+1
    arr = [0] * (n + 1)
    for i in range(1, n + 1):
        arr[i] = int(input_data[ptr])
        ptr += 1
    
    limit = 16
    log2 = [0] * (n + 1)
    stmax = [[0] * limit for _ in range(n + 1)]
    stmin = [[0] * limit for _ in range(n + 1)]

    log2[0] = -1
    for i in range(1, n + 1):
        log2[i] = log2[i >> 1] + 1
        stmax[i][0] = arr[i]
        stmin[i][0] = arr[i]
    
    for p in range(1,limit):
        for i in range(1, n - (1 << p) + 2):
            stmax[i][p] = max(stmax[i][p - 1], stmax[i + (1 << (p - 1))][p - 1])
            stmin[i][p] = min(stmin[i][p - 1], stmin[i + (1 << (p - 1))][p - 1])
    
    def query(l, r):
        length = r - l + 1
        p = log2[length]
        max_val = max(stmax[l][p], stmax[r - (1 << p) + 1][p])
        min_val = min(stmin[l][p], stmin[r - (1 << p) + 1][p])
        return max_val - min_val

    res = []
    for _ in range(m):
        l = int(input_data[ptr])
        r = int(input_data[ptr + 1])
        ptr += 2
        res.append(str(query(l, r)))
    