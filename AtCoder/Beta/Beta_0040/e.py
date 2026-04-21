import sys

n,q = list(map(int,sys.stdin.readline().split()))
mp = set()
people = []
for _ in range(n):
    x,v = list(map(int,sys.stdin.readline().split()))
    mp.add(x)
    mp.add(v)
    people.append(list(map(int,sys.stdin.readline().split())))

que = []
for _ in range(q):
    l,r = list(map(int,sys.stdin.readline().split()))
    mp.add(l)
    mp.add(r)
    que.append(list(map(int,sys.stdin.readline().split())))

ranks = {x:i+1 for i,x in enumerate(sorted(mp))}
rp = []
for x,v in people:
    rp.append([ranks[x],ranks[v]])

rq = []
for l,r in que:
    rq.append([ranks[l],ranks[r]])

res = []
