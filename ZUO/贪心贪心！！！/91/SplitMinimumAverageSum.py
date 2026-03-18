#  平均值最小累加和
#  给定一个数组arr，长度为n
#  再给定一个数字k，表示一定要将arr划分成k个集合
#  每个数字只能进一个集合
#  返回每个集合的平均值都累加起来的最小值
#  平均值向下取整
#  1 <= n <= 10^5
#  0 <= arr[i] <= 10^5
#  1 <= k <= n
#  来自真实大厂笔试，没有在线测试，对数器验证
#还是正男则反，贪心思路，灵感是，最小的k-1个数字为1分
#最后把所有剩下的数字为一组，不让他拉高平均值

def minAverageSum2(arr, k):
    arr.sort()
    
    ans = 0
    
    # 前 k-1 个最小的数，各自单独成组
    for i in range(k - 1):
        ans += arr[i]
    
    # 剩下的合成一个组
    total = 0
    for i in range(k - 1, len(arr)):
        total += arr[i]
    
    ans += total // (len(arr) - k + 1)
    
    return ans