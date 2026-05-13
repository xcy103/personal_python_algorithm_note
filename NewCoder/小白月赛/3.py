import sys

n = int(input())

res = []
for _ in range(n):
    l,r = map(int,input().split())
    if r<=1:
        res.append('0')
        continue
    
    op = 0
    lo = max(l.bit_length(),1)
    hi = r.bit_length()-1
    
    if lo<hi:
        op+=(lo+hi-1)*(hi-lo)//2
        low_i = 0
        while ((1<<(lo-1))+(1<<low_i))<1<<lo:
            if ((1<<(lo-1))+(1<<low_i))>=l:
                op+=1
            low_i+=1
    if 1<<hi==r:
        op+=1
    high_i = 0
    while (1<<hi)+(1<<high_i)<=r:
        op+=1
        high_i+=1
    res.append(str(op))

print('\n'.join(res))

