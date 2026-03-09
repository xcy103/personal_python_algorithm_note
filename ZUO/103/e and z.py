#运用z数组的题目，2223. Sum of Scores of Built Strings
#如果不太理解，建议再从manacher开始看起，顺便把kmp也看了
#z数组就是求s，从i开始能和原字符串匹配多大的长度,z[0]当然是原数组长度n
#这里有还有两个变量，一个是r,表示现在扩充到的右边界
#一个是c，表示扩充到这个右边界r时候的起点,注意有边界是不能达到的
#有两种情况，当起点为i
#1.i在r之内，i<r，我们需要找到关键点i-c，当前起点匹配的长度就是z[i-c]和r-i的最小值
#2.i在r上或者i大于r，这个时候就要暴力匹配了，从长度为0开始

class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        z = [0] * n
        z[0] = n
        c = 1
        r = 1
        for i in range(1,n):
            t = 0 if r<=i else min(r-i,z[i-c])
            while i+t<n and s[i+t]==s[t]:
                t+=1
            if i+t>r:
                r = i+t
                c = i
            z[i] = t
        return sum(z)


#e数组求法
a = []
b = []
n,m = len(a),len(b)
#先求B的z数组
z=[0]*m
z[0] = m
r,c = 1
for i in range(1,m):
    t = 0 if r<=i else min(r-i,z[i-c])  
    while i+t<m and b[i+t]==b[t]:
        t+=1
    if i+t>r:
        c = i
        r = i+t
    z[i] = t
#然后再拿B的z数组去求A的e数组
e = [0]*n
c,r = 0
for i in range(n):
    t = 0 if r<=i else min(r-i,z[i-c])
    while i+t<n and t<m and a[i+t]==b[t]:
        t+=1
    if i+t>r:
        c = i
        r = i+t
    e[i] = t
