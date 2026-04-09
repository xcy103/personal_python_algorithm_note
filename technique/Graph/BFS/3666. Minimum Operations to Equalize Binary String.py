from collections import Counter
nums = [1,3,4,1,2,3,1]
n = len(nums)
if len(set(nums))==n:
     [nums]
c = Counter(nums)
mx = max(c.values())
res = [[] for _ in range(mx)]
i = 0
while len(c)>0:
    t = []
    for k in c.keys():
        if c[k]==0:continue
        res[i].append(k)
        c[k]-=1
        if c[k]==0:
            t.append(k)
        i+=1
    for k in t:
        c.pop(k)
