import sys
input = sys.stdin.readline
#傻逼规律
def f(x):
    if x % 4 == 0: return x
    if x % 4 == 1: return 1
    if x % 4 == 2: return x + 1
    return 0

t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    print(f(r) ^ f(l - 1))