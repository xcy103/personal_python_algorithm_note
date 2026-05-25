import sys

n = int(input())

if n>3:
    print(-1)
    exit(0)

else:
    if n==1:
        print(1)
    elif n==2:
        print('1 2')
        print('3 4')
    elif n==3:
        print('1 2 3')
        print('5 4 6')
        print('7 8 9')
