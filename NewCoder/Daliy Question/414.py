import sys
from collections import Counter
n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().split()))

c = Counter(arr)
t = n//9
c0 = 0
c1 = 0
for k,v in c.items():
    if v==t:
        c0+=1
    elif v==t+1:
        c1+=1
if c1==n%9 and c0==9-(n%9):
    print('YES')
else:
    print('NO')
