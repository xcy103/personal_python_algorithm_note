s = "aaaa"
seen = set()
n  = len(s)
res = []
i = 0
while i<n:
    j = i+1
    while j<=n and s[i:j] in seen:
        j+=1
    if j==n and s[i:j] in seen:
        break
    res.append(s[i:j])
    seen.add(s[i:j])
    i = j
res