import array
import math
import sys
from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = array.array('i', map(int,input().split()))
    a = sorted(a)
    # print(a)
    con = Counter(a)
    # print(con)
    s = list(con.keys())
    l = len(s)
    # print(s)

    if 1 in con and con[1] >= 2:
        print('YES')
        continue
    ff = 0
    if 1 in con and con[1] == 1:
        for i in range(1, l):
            if con[s[i]] >= 2:
                ff = 1
    if ff:
        print('YES')
        continue

    f = 0

    for i in range(l):
        if s[i] == 1:
            continue
        for j in range(2, 31):
            res = pow(s[i], j)
            if res > 10**9:
                break
            if j in con and res in con:
                f = 1
                break
        if f:
            break

    if f:
        print('YES')
    else:
        print('NO')