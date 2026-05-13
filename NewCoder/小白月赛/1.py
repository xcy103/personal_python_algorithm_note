import sys

rate = [0]*7

n = int(input())
arr = list(map(int,input().split()))

init = 1000
for x in arr:
    init+=x
    if init<700:
        rate[0]+=1
    elif 700<=init<1000:
        rate[1]+=1
    elif 1000<=init<1500:
        rate[2]+=1
    elif 1500<=init<2000:
        rate[3]+=1
    elif 2000<=init<2400:
        rate[4]+=1
    elif 2400<=init<2800:
        rate[5]+=1
    else:
        rate[6]+=1
print(*rate)
     