#  过河问题
#  一共n人出游，他们走到一条河的西岸，想要过河到东岸
#  每个人都有一个渡河时间ti，西岸有一条船，一次最多乘坐两人
#  如果船上有一个人，划到对岸的时间，等于这个人的渡河时间
#  如果船上有两个人，划到对岸的时间，等于两个人的渡河时间的最大值
#  返回最少要花费多少时间，才能使所有人都过河
#  测试链接 : https://www.luogu.com.cn/problem/P1809
import sys

def minCost(nums, n):
    nums.sort()
    dp = [0] * n

    if n >= 1:
        dp[0] = nums[0]
    if n >= 2:
        dp[1] = nums[1]
    if n >= 3:
        dp[2] = nums[0] + nums[1] + nums[2]

    for i in range(3, n):
        # 两种策略取最优
        dp[i] = min(
            dp[i - 1] + nums[i] + nums[0],
            dp[i - 2] + nums[1] * 2 + nums[i] + nums[0]
        )

    return dp[n - 1]


def main():
    data = list(map(int, sys.stdin.read().split()))
    idx = 0
    res = []

    while idx < len(data):
        n = data[idx]
        idx += 1
        nums = data[idx:idx + n]
        idx += n
        res.append(str(minCost(nums, n)))

    print("\n".join(res))


if __name__ == "__main__":
    main()