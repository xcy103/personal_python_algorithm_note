import sys

n,m = map(int,sys.stdin.readline().split())
can = [True] * (m+1)
people = []
for _ in range(n):
    t = int(sys.stdin.readline().strip())
    people.append(list(map(int,sys.stdin.readline().split())))

res = []
for p in people:
    f = 1
    for x in p:
        if can[x]:
            f = 0
            res.append(str(x))
            can[x] = False
            break
    if f:
        res.append(str(0))

print('\n'.join(res))