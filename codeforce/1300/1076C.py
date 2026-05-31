import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    d = int(input())
    if d == 0:
        print("Y 0 0")
        continue
    if d < 4:
        print("N")
        continue

    import math
    s = math.sqrt(d * d - 4 * d)
    a = (d + s) / 2
    b = (d - s) / 2
    print("Y", a, b)