import sys

t = int(input())

res = []
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    #感觉像是线段树或者树状数组优化DP
    mp = {}
    for x in arr:
        tmp = 1
        if x+1 in mp:
            tmp = max(mp[x+1]+1,tmp)
        if x-1 in mp:
            tmp = max(mp[x-1]+1,tmp)
        mp[x] = tmp

    res.append(str(max(mp.values())))

print('\n'.join(res))