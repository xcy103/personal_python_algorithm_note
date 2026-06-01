import sys
from math import sin, radians

n, r = map(int, input().split())

x = sin(radians(180 / n))   # π/n

print(r * x / (1 - x))