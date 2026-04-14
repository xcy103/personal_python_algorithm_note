
def canMakeSubsequence(str1: str, str2: str) -> bool:
    n = len(str1)
    m = len(str2)
    l = 0
    r = 0
    s1 = list(str1)
    s2 = list(str2)
    while l<n and r<m:
        if (ord(s1[l])+1)%26==ord(s2[r]):
            r+=1
        elif ord(s1[l])==ord(s2[r]):
            r+=1
        l+=1
    return r==m

canMakeSubsequence("abc","ad")