import sys

n = int(input())

if n<=2:
    print('No Answer')
else:
    res = []
    if n%2==0:
        s = n//2
        if s%2==1:
            for i in range(s//2+1):
                res+=[-3,2]
            for i in range(s//2-1):
                res+=[-1,2]
            res+=[-1,3]
        else:
            for i in range(s//2):
                res+=[-3,2]
            for i in range(s//2):
                res+=[-1,2]
    else:
        if n==3:
            res = [-1,3,-2]
        elif n==5:
            res = [2,-3,2,-3,2]
        else:
            s = (n-1)//2
            if s%2==0:
                for i in range(s//2+1):
                    res+=[2,-3]
                for i in range(s//2-1):
                    res+=[2,-1]
                res+=[2]
            else:
                for i in range(s//2+1):
                    res+=[2,-3]
                for i in range(s//2):
                    res+=[3,-2]
                res+=[1]
print(*res)
print(sum(res))

