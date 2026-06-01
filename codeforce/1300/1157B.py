import sys

n = int(input())
s = list(map(int,input().split()[0]))
mp = [0]+list(map(int,input().split()))

l = 0
while l<n:
    if l<n and s[l]<mp[s[l]]:
        r = l
        while r<n and s[r]<=mp[s[r]]:
            s[r] = mp[s[r]]
            r+=1
        break
    l+=1
print(''.join(list(map(str,s))))