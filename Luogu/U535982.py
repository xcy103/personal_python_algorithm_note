import sys

t = int(sys.stdin.readline().strip())
res = []
arr = []
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    arr.append(sys.stdin.readline().strip())

def f(s,tar):
    op = 0
    for i in range(len(s)):
        if s[i]!=tar[i]:
            op+=1
    return op//2
for s in arr:
    s = list(s)
    s1 = list('AB'*(len(s)//2))
    s2 = list('BA'*(len(s)//2))
    res.append(str(min(f(s,s1),f(s,s2))))

print('\n'.join(res))