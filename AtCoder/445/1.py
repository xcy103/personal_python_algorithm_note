import sys

s = sys.stdin.readline().strip()

ans = s[0]==s[-1]
print('Yes' if ans else 'No')