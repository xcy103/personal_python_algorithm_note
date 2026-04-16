

import sys

h,w = list(map(int, sys.stdin.readline().split()))

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]

row_sum = [sum(arr[i]) for i in range(h)]
col_sum = [sum((arr[i][j]) for i in range(h)) for j in range(w)]

ans = 0
for mask in range(1<<h):
    cur = 0
    #行贡献
    for i in range(h):
        if mask>>i&1:
            cur+=row_sum[i]
    #列贡献
    #这道题我没想到的点就是这里
    #其实不用再用mask去枚举列，我们可以顺序枚举
    #如果当前列的贡献大于0，我们就加上
    #仔细想想，我们就可以不用枚举所有列的状态
    for j in range(w):
        c = 0
        for i in range(h):
            if mask>>i&1:
                c+=arr[i][j]
        gain = col_sum[j] - c

        if gain>0:
            cur+=gain
    ans = max(cur,ans)