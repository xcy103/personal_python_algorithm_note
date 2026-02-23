import sys
from collections import defaultdict
n,m = map(int,sys.stdin.readline().split())
s,t = map(int,sys.stdin.readline().split())

d = defaultdict(int)
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    d[a]+=b

op = 0
# if s==t:
#     op = d[s]
# elif s<t:
#     for i in range(s,t+1):
#         op+=d[i]
# else:
#     for i in range(s,t-1,-1):
#         op+=d[i]
if s>t:
    s,t = t,s
for k,v in d.items():
    if k>=s and k<=t:
        op+=v
print(op)
    