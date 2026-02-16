import sys

# data = sys.stdin.read().strip().split()
# ptr = 0
# n,m = int(data[ptr:ptr+2])
# ptr+=2

# s1 = set(list(map(int,data[ptr:ptr+n])))
# ptr+=n

# s2 = set(list(map(int,data[ptr:ptr+m])))
# ptr+=m

# q = int(data[ptr])
# ptr+=1
# ret = []
n,m = map(int,sys.stdin.readline().split())
s1 = set(list(sys.stdin.readline().split()[0]))
s2 = set(list(sys.stdin.readline().split()[0]))
q = int(sys.stdin.readline().strip())
ret = []
for _ in range(q):
    
    # s = set(list(map(int,data[ptr:ptr+n])))
    s = set(list(sys.stdin.readline().strip().split()[0]))
    # ptr+=1
    if s|s1==s1 and s|s2!=s2:
        ret.append('Takahashi')
    elif s|s2==s2 and s|s1!=s1:
        ret.append('Aoki')
    else:
        ret.append('Unknown')

sys.stdout.write('\n'.join(ret))