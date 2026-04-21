import sys

mp = {}
n = int(sys.stdin.readline().strip())
res = []
for _ in range(n):
    ops = sys.stdin.readline().split()
    op = ops[0]
    if op=='1':
        mp[ops[1]] = ops[2]
        res.append('OK')
    elif op=='2':
        if ops[1] not in mp:
            res.append('Not found')
        else:
            res.append(mp[ops[1]])
    elif op=='3':
        if ops[1] not in mp:
            res.append('Not found')
        else:
            del mp[ops[1]]
            res.append('Deleted successfully')
    elif op=='4':
        res.append(str(len(mp)))

print('\n'.join(res))

