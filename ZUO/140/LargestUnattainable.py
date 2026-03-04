# 无法组成的最大值
# 一共有a、b两种面值的硬币，a和b一定互质，每种硬币都有无限个
# 返回a和b无法组成的钱数中，最大值是多少
# 题目的输入保证存在最大的无法组成的钱数
# 1 <= a、b <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P3951
#非常考察灵感，首先有ax+by = c
#当c无法由啊，b组成时候，必然有x=-1或者y=-1
#然后我们就看y可以是那些数字，最大取到a-1
import sys

a,b = map(int,sys.stdin.readline().split())

print(a*b-a-b)