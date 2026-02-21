import sys

n = int(sys.stdin.readline().strip())

res = []
for _ in range(n):
    _ = map(int,sys.stdin.readline().strip())
    arr = set(map(int,sys.stdin.readline().split()))
    if 67 in arr:
        res.append('Yes')
    else:
        res.append('No')

print('\n'.join(res))