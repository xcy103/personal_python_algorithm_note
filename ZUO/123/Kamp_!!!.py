import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

n, k = map(int, input().split())

g = [[] for _ in range(n+1)]

for _ in range(n-1):
    u,v,w = map(int, input().split())
    g[u].append((v,w))
    g[v].append((u,w))

people = [0]*(n+1)
arr = list(map(int, input().split()))
for x in arr:
    people[x] += 1

incost = [0]*(n+1)
inner1 = [0]*(n+1)
inner2 = [0]*(n+1)
choose = [0]*(n+1)

outcost = [0]*(n+1)
outer = [0]*(n+1)

def dfs1(u,f):
    for v,w in g[u]:
        if v==f:
            continue
        dfs1(v,u)
        people[u]+=people[v]

        if people[v]>0:
            incost[u]+=incost[v]+2*w
            longest = inner1[v] + w

            if longest > inner1[u]:
                choose[u] = v
                inner2[u] = inner1[u]
                inner1[u] = longest
            elif longest > inner2[u]:
                inner2[u] = longest

def dfs2(u,f):
    for v,w in g[u]:
        if v==f:
            continue
        if k-people[v]>0:
            if people[v]==0:
                outcost[v] = outcost[u] + incost[u] + w*2
            else:
                outcost[v] =  outcost[u] + incost[u] - incost[v]
            
            if v!=choose[u]:
                outer[v] = max(outer[u], inner1[u]) + w
            else:
                outer[v] = max(outer[u], inner2[v]) + w
            
            dfs2(v,u)

dfs1(1,0)
dfs2(1,0)

for i in range(n+1):
    print(outcost[i], outer[i] - max(inner1[i], outer[i]))