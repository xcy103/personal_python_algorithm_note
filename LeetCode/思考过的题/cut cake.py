m =6
n =3
h =[2,3,2,3,1]
v =[1,2]
h.sort()
v.sort()
th = tv = 1
l = 0
r = 0
res = 0
while l<m-1 and r<n-1:
    if h[l]>v[r]:
        res+=h[l]*tv
        l+=1
        th+=1
    else: #h[l]<v[r]:
        res+=v[r]*th
        r+=1
        tv+=1
while l<m-1:
    res+=h[l]*tv
    l+=1
while r<n-1:
    res+=v[r]*th
    r+=1
print(res)