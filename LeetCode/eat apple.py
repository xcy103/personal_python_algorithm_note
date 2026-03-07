s ="ababc"
word ="ab"
n = len(s)
m = len(word)
k = 0
while m*k<=n:
    if k>0 and word*k in s:
        print(k)
    k+=1
print( 0 if m*k<=n else 0)