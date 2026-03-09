
def manacher(s: str):
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0]*n
    c = r = ans = 0

    for i in range(n):
        p[i] = 1 if r<=i else min(p[2*c-i], r-i)

        while i-p[i]>=0 and i+p[i]<n and t[i-p[i]]==t[i+p[i]]:
            p[i] += 1

        if i+p[i]>r:
            r = i+p[i]
            c = i
        ans = max(ans, p[i])
    
    return ans-1
    
manacher("abaccdbbd")