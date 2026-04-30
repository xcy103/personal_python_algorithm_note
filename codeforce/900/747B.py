import sys
from collections import Counter
n = int(sys.stdin.readline().strip())
s = list(sys.stdin.readline().split()[0])

c = Counter(s)

if len(s)%4:
    print("===")
    exit(0)

t = len(s)//4
ta = c['A']
tc = c['C']
tg = c['G']
tt = c['T']
t_ = c['?']


if ta>t or tc>t or tg>t or tt>t:
    print("===")
    exit(0)

res = []
res+=(t-ta)*['A']
res+= (t-tt)*['T']
res+= (t-tg)*['G']
res+= (t-tc)*['C']
l = 0
r = 0
n = len(s)
while r<n:
    if s[r]=='?':
        s[r] = res[l]
        l+=1
    r+=1
print(''.join(s))