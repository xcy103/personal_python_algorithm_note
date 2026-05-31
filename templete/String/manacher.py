# 计算最长 prefix == suffix
lps = [0]*n
j = 0
for i in range(1,n):
    while j>0 and s[i]!=s[j]:
        j = lps[j-1]
    if s[i]==s[j]:
        j+=1
    lps[i]=j

overlap = lps[-1]