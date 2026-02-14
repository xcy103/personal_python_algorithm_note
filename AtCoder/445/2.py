import sys

n = int(sys.stdin.readline().strip())

strs = []
m = 0
for _ in range(n):
    s = sys.stdin.readline().strip()
    m = max(len(s),m)
    strs.append(s)

ans = []
for s in strs:
    
    t = (m-len(s))//2
    ans.append('.'*t+s+'.'*t)

sys.stdout.write('\n'.join(ans)+'\n')