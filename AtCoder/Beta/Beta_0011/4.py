import sys

n,q = map(int, sys.stdin.readline().split())
vals = list(map(int, sys.stdin.readline().split()))
people = list(map(int, sys.stdin.readline().split()))
queries = []
for _ in range(q):
    queries.append(int(sys.stdin.readline().strip()))

people = [0,0]+people
vals = [0]+vals

dis = [0]*(n+1)

for i in range(1,n+1):
    dis[i] += dis[people[i]] + vals[i]

res = []
for q in queries:
    res.append(str(dis[q]))

print("\n".join(res))
