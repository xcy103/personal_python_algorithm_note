import sys
s = sys.stdin.readline().split()
s = set(list(s)[0])
print('Yes' if (s | {'r','e','d'}=={'r','e','d'}) else 'No')