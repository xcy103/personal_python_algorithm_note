import sys
from collections import defaultdict,Counter
n,m = map(int,sys.stdin.readline().split())
seats = []
for _ in range(n):
    seats.append(list(sys.stdin.readline().split()[0]))

drow = defaultdict(Counter)
dcol = defaultdict(Counter)
for i in range(n):
    for j in range(m):
        drow[i][ord(seats[i][j])-ord('a')]+=1
for j in range(m):
    for i in range(n):
        dcol[j][ord(seats[i][j])-ord('a')]+=1

res = []
for i in range(n):
    for j in range(m):
        if drow[i][ord(seats[i][j])-ord('a')]==1 and dcol[j][ord(seats[i][j])-ord('a')]==1:
            res.append(seats[i][j])

print(''.join(res) if res else "")