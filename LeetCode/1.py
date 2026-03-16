from collections import Counter
mp = set()
for i in range(15*9+1):
    s = list(str(i))
    n = len(s)
    if n==1: mp.add(i)
    else:
        if n==2:
            s0 = s[0]
            s1 = s[1]
            if s0<s1 or s1<s0:
                mp.add(i)
        else:
            s0 = s[0]
            s1 = s[1]
            s2 = s[2]
            if s0<s1<s2 or s0>s1>s2:
                mp.add(i)
                
print(mp)
            