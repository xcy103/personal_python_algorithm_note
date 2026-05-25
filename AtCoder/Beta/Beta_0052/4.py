import sys

n, m = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(list(map(int, input().split())))

t = n

for mask in range(1 << n):
    ok = True
    for i in range(m):
        k = arr[i][0]
        nodes = arr[i][1:1+k]
        r = arr[i][-1]

        ans = 0
        for x in nodes:
            ans |= (mask >> (x-1)) & 1

        if (ans > 0) != (r == 1):
            ok = False
            break

    if ok:
        t = min(t, bin(mask).count('1'))

print(t)