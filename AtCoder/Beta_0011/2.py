# import sys

# h,w,k = map(int,sys.stdin.readline().split())
# c1,c2 = sys.stdin.readline().split()
# arr = []
# for _ in range(h):
#     arr.append(sys.stdin.readline().strip())

# res = [['']*(w*k) for _ in range(h*k)]
# for i in range(h):
#     for j in range(w):
#         if arr[i][j]=='#':
#             for x in range(k):
#                 for y in range(k):
#                     res[i*k+x][j*k+y] = c1
#         else:
#             for x in range(k):
#                 for y in range(k):
#                     res[i*k+x][j*k+y] = c2

# print('\n'.join(''.join(line) for line in res))
# H,W<=1000
# K<=50
# 注意下这道题，算是语法题，如果按照每个位置赋值然后再输出
# 太慢了，可以直接拓展然后打印
H, W, K = map(int, input().split()) 
c1, c2 = input().split() 
grid = [input() for _ in range(H)] 

for i in range(H): 
    expanded_row = [] 
    for j in range(W): 
        char = c1 if grid[i][j] == '#' else c2 
        expanded_row.append(char * K) 
    expanded_line = ''.join(expanded_row) 
    for _ in range(K): 
        print(expanded_line)

H, W, K = map(int, input().split()) 
c1, c2 = input().split() 
grid = [input() for _ in range(H)] 

