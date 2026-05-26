import sys

n = int(input())
arr = list(map(int,input().split()))
prize = list(map(int,input().split()))

res = [0]*5
num = 0
for x in arr:
    tmp = x+num
    num = 0
    for i,y in enumerate(prize[::-1]):
        if tmp>=y:
            res[4-i]+=tmp//y
            tmp = tmp - tmp//y*y
    num+=tmp
print(*res)
print(num)
