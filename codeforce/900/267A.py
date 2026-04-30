import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())
    a,b = max(a,b),min(a,b)

    op = 0
    while a and b:
        op+=a//b
        a,b = b,a%b

    print(op)
        