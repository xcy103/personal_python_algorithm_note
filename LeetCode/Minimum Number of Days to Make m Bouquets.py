bloomDay = [1,10,3,10,2]
m = 3
k = 1
n = len(bloomDay)
if m*k>n:
    print(-1)
bloomDay.sort()
i = 0
op = 0
while i<n:
    cur = bloomDay[i]
    l = 1
    while i<n-1 and bloomDay[i+1]<=cur+1:
        i+=1
        l+=1
        cur = bloomDay[i]
    op+=l//k    
    i+=1
print(1)