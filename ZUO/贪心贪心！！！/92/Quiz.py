#  知识竞赛
#  最近部门要选两个员工去参加一个需要合作的知识竞赛，
#  每个员工均有一个推理能力值ai，以及一个阅读能力值bi
#  如果选择第i个人和第j个人去参加竞赛，
#  两人在推理方面的能力为X = (ai + aj)/2
#  两人在阅读方面的能力为Y = (bi + bj)/2
#  现在需要最大化他们表现较差一方面的能力
#  即让min(X,Y) 尽可能大，问这个值最大是多少
#  测试链接 : https://www.nowcoder.com/practice/2a9089ea7e5b474fa8f688eae76bc050
#  请同学们务必参考如下代码中关于输入、输出的处理
#太骚了，根据差值绝对值升序排序
#来到一个人
n = int(input())
a = [[] for i in range(n)]

for i in range(n):
    a[i] = input().split()

for i in range(n):
    for j in range(len(a[i])):
        a[i][j] = int(a[i][j])

a.sort(key = lambda x:abs(x[0]-x[1]))
mx1 = [0]*n
mx2 = [0]*n
mx1[0] = a[0][0]
mx2[0] = a[0][1]
ans = 0
for i in range(1,n):
    if a[i][0]<a[i][1]:
        ans = max(ans,mx1[i-1]+a[i][0])
    else:
        ans = max(ans,mx2[i-1]+a[i][1])
    mx1[i] = max(mx1[i-1],a[i][0])
    mx2[i] = max(mx2[i-1],a[i][1])
print(ans/2.0)