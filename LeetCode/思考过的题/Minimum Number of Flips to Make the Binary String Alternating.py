s= "01001001101"
s= list(s)
n = len(s)
print(n)
res = float('inf')
def check(arr):
    op1 = 0
    f1 = "0"
    for i in range(n):
        if arr[i]!=f1:
            op1+=1
        f1 = "1" if f1=="0" else "0"
    op2 = 0
    f2 = "1"
    for i in range(n):
        if arr[i]!=f2:
            op2+=1
        f2 = "1" if f2=="0" else "0"
    return op1,op2
# for i in range(n):
#     print(check(s),s[0])
#     s = s[1:] + [s[0]]
dp = [[0,0] for _ in range(n)]
dp[0][0],dp[0][1] = check(s)
print(dp[0])
#res = min(res,op1,op2)
for i in range(1,n):
    # if n%2==0:
    #     dp[i][0] = dp[i-1][1]+(-1 if int(s[i-1])==1 else +1)
    #     dp[i][1] = dp[i-1][0]+(-1 if int(s[i-1])==0 else +1)
    
    dp[i][0] = dp[i-1][1]+(-1 if int(s[i-1])==0 else +1)
    dp[i][1] = dp[i-1][0]+(-1 if int(s[i-1])==1 else +1)
    res = min(res,min(dp[i]))
    print(dp[i][0],dp[i][1],res)
# s= "01001001101"
# s = list(s)
# n = len(s)
# res = float('inf')
# dp = [[0,0]]*n
# op1 = 0
# f1 = "0"
# for i in range(n):
#     if s[i]!=f1:
#         op1+=1
#     f1 = "1" if f1=="0" else "0"
# op2 = 0
# f2 = "1"
# for i in range(n):
#     if s[i]!=f2:
#         op2+=1
#     f2 = "1" if f2=="0" else "0"
# if n%2==0:
#     print( min(op1,op2))
# else:
#     dp[0][0] = op1
#     dp[0][1] = op2
#     res = min(res,op1,op2)
#     for i in range(1,n):
#         dp[i][0] = dp[i-1][1]+(-1 if int(s[i-1])==0 else +1)
#         dp[i][1] = dp[i-1][0]+(-1 if int(s[i-1])==1 else +1)
#         res = min(res,dp[i][0],dp[i][1])
#         print(res,dp[i][0],dp[i][1])



   