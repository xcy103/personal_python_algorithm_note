import sys

t = int(input())

res = []
for _ in range(t):
    n = int(input())
    s = input().strip()
    s = list('0'+s+'0')
    f = 1
    for i in range(1,n+1):
        if s[i]=='1' and s[i-1]=='0' and s[i+1]=='0':
            f = 0
            res.append('NO')
            break
    if f:
        res.append('YES')
print('\n'.join(res))