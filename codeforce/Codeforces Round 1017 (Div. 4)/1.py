import sys

n = int(sys.stdin.readline().strip())
arr = []
for i in range(n):
    arr.append(sys.stdin.readline().split())

ret = []
for s in arr:
    ret.append(s[0][0]+s[1][0]+s[2][0])

print('\n'.join(ret))
