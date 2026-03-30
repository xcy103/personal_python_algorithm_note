#  E&D游戏
#  桌子上有2n堆石子，编号为1、2、3...2n
#  其中1、2为一组；3、4为一组；5、6为一组...2n-1、2n为一组
#  每组可以进行分割操作：
#  任取一堆石子，将其移走，然后分割同一组的另一堆石子
#  从中取出若干个石子放在被移走的位置，组成新的一堆
#  操作完成后，组内每堆的石子数必须保证大于0
#  显然，被分割的一堆的石子数至少要为2
#  两个人轮流进行分割操作，如果轮到某人进行操作时，所有堆的石子数均为1，判此人输掉比赛
#  返回先手能不能获胜
#  测试链接 : https://www.luogu.com.cn/problem/P2148
#   通过观察sg表，我们得出最低a-1的0所在的位，就是sg的值
import sys

def lowZero(status: int) -> int:
    ans = 0
    while status > 0:
        if (status & 1) == 0:
            break
        status >>= 1
        ans += 1
    return ans



t = int(sys.stdin.readline().strip())

res = []
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    arr = list(map(int,sys.stdin.readline().split()))
    s = 0
    for i in range(0,n,2):
        s^=lowZero((arr[i]-1)|arr[i+1]-1)
    if s != 0:
        res.append("YES")
    else:
        res.append("NO")

sys.stdout.write("\n".join(res))

