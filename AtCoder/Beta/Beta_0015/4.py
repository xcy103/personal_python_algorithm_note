import sys

n,m,c = map(int,sys.stdin.readline().split())
staff = list(map(int,sys.stdin.readline().split()))
dish = list(map(int,sys.stdin.readline().split()))
staff.sort()
dish.sort()

n1 = len(staff)
n2 = len(dish)

op = 0
l = 0
r = 0
while l < n1 and r < n2:
    if staff[l]>= dish[r]:
        op+=1
        l+=1
        r+=1
    elif staff[l]<dish[r]:
        l+=1
print(op*c)