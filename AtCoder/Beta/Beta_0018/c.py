import sys
n,q = map(int,sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(sys.stdin.readline().strip())
f = list(range(26))
for i in range(q):
    a,b = sys.stdin.readline().split()
    f[ord(a)-ord('a')] = ord(b)-ord('a')

def find(i):
    while i!=f[i]:
        f[i] = f[f[i]]
        i = f[i]
    return f[i]
for i in range(26):
    f[i] = find(i)

res = []
for i in range(n):
    arr[i] = list(arr[i])
    for j in range(len(arr[i])):
        arr[i][j] = chr(f[ord(arr[i][j]) - ord('a')] + ord('a'))
    print(''.join(arr[i]))
