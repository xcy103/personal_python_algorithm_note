import sys
from collections import defaultdict,Counter
t = int(input())

st = []
xor = 0
d = Counter()
res = []
i = 1
for _ in range(t):
    ops = list(input().split())
    if ops[0]=='PUT':
        st.append(int(ops[1]))
        xor^=int(ops[1])
    elif ops[0]=='REMOVE':
        xor^=st.pop()
    else:
        if xor not in d:
            res.append(-1)
        else:res.append(d[xor])
        d[xor] = i
        i+=1
print('\n'.join(list(map(str,res))))