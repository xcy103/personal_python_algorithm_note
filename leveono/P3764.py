#就是一个取模
import sys

s = sys.stdin.readline().strip()
l,r = map(int,sys.stdin.readline().split())
cb = s.count('B')
n = len(s)
if r-l<=n:
    l%=n
    l+=1
    r%=n
    r+=1
    op = 0
    print(s[(l-1):r].count('B'))
else:
    t = (r-l)//n
    l%=n
    l+=1
    r%=n
    r+=1
    p1 = s[(l-1):].count('B')
    p2 = s[:r].count('B')
    print(p1+p2+t*cb)