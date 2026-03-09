s = "43987654"
a = 7
b = 3
n = len(s)
t = list(s)
t = list(map(int,t))
res = s[:]
for loop in range(n):
    tmp = t[:]
    for _ in range(10):
        op = float('inf')
        for i in range(1,n,2):
            tmp[i] = (tmp[i]+a)%10
        res = min(res, "".join(map(str,tmp)))
    t = t[n-b:] + t[:n-b]
print(res)