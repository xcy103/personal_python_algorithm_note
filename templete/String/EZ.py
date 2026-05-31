n,m = len(a),len(b)
#先求B的z数组
z=[0]*m
z[0] = m
r = c = 1
for i in range(1,m):
    t = 0 if r<=i else min(r-i,z[i-c])  
    while i+t<m and b[i+t]==b[t]:
        t+=1
    if i+t>r:
        c = i
        r = i+t
    z[i] = t
#然后再拿B的z数组去求A的e数组
e = [0]*n
c = r = 0
for i in range(n):
    t = 0 if r<=i else min(r-i,z[i-c])
    while i+t<n and t<m and a[i+t]==b[t]:
        t+=1
    if i+t>r:
        c = i
        r = i+t
    e[i] = t