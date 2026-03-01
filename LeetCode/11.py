MOD = 10**9+7
k = 10
l = r = 5
s = (r-l+1)*(r+l)//2
if r-l+1==1:
    one = s
else:one = (k-1)*(r-l+1)*s%MOD
res = 0
for i in range(0,k,2):
    res = (res*10 + one)%MOD
    res = (res*10 + one)%MOD
print(res)