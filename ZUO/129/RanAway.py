import sys

input = sys.stdin.readline

MAXP = 64
INF = 10**18

n = int(input())
m = int(input())

stjump = [[[False]*(MAXP+1) for _ in range(n+1)] for _ in range(n+1)]

time = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    u,v = map(int,input().split())
    stjump[u][v][0] = True
    time[u][v] = 1

for p in range(1,MAXP+1):
    for jump in range(1,n+1):
        for i in range(1,n+1):
            if not stjump[i][jump][p - 1]:
                continue
            for j in range(1,n+1):
                if stjump[jump][j][p-1]:
                    stjump[i][j][p] = True
                    time[i][j] = 1


for jump in range(1,n+1):
    for i in range(1,n+1):
        if time[i][jump] == INF:
            continue
        for j in range(1,n+1):
            if time[jump][j] == INF:
                continue
            time[i][j] = min(time[i][j], time[i][jump] + time[jump][j])
    
print(time[1][n])

