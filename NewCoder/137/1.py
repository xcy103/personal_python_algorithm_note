import sys

num = int(input())

a = num//3600
b = (num-a*3600)//60

c = num - a*3600 - b*60

print(a,b,c)