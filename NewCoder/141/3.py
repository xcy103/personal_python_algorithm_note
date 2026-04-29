import sys

t = int(sys.stdin.readline().strip())

res = []

for _ in range(t):
    s = list(sys.stdin.readline().strip())
    
    n = len(s)
    l = 0
    r = n-1
    while l<r:
        if s[l]==s[r]:
            l+=1
            r-=1
        else:
            if s[l]=='n' and s[r]=='m':
                if l+1<n and s[l+1]=='n':
                    l+=2
                    r-=1
                else:
                    res.append('NO')
                    break
            elif s[l]=='m' and s[r]=='n':
                if r>0 and s[r-1]=='n':
                    r-=2
                    l+=1
                else:
                    res.append('NO')
                    break
print('\n'.join(res))