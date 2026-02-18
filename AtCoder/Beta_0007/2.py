import sys

n,k = map(int,sys.stdin.readline().split())
ans = []
base = 2333
for _ in range(n):
    m = int(sys.stdin.readline().strip())
    words = list(sys.stdin.readline().split())
    tmp = []
    for word in words:
        h = 0
        for c in word:
            h = (h * base + ord(c)) % 1000000007
        tmp.append(h)
    ans.append(set(tmp))

op = 0
for i in range(n-1):
    for j in range(i+1,n):
        if len(ans[i]&ans[j])>=k:
            op += 1
print(op)
