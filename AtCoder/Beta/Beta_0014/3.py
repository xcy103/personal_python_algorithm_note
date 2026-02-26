import sys

g,m,d,k,v = map(int,sys.stdin.readline().split())

t1 = (m-g)/v

if d*k>=g:
    #t2 = g/d
    x = g*v
    y = (m-g)*d
    print('Yes' if x<=y else 'No')
else:
    t2 = k+(g-d*k)
    x = t2*v
    y = (m-g)
    print('Yes' if x<=y else 'No')