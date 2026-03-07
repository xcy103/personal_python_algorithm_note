import sys

n = int(sys.stdin.readline())

c = 1
for i in range(1, n + 1):
    c = c * (4 * i - 2) // (i + 1)

print(c)