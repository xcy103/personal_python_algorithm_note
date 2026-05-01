import sys

t = int(input())

ans = []
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr = sorted(set(arr))
    
    res = []
    l = 0
    for i,x in enumerate(arr):
        if not res:
            res.append(x)
            l+=1
        else:
            if x-res[-1]>=l:
                res.append(x)
                l+=1
    
    ans.append(str(len(res)))

print('\n'.join(ans))

