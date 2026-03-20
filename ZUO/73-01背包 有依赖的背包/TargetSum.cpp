// 新思路，转化为01背包问题
// 思考1:
// 虽然题目说nums是非负数组，但即使nums中有负数比如[3,-4,2]
// 因为能在每个数前面用+或者-号
// 所以[3,-4,2]其实和[3,4,2]会达成一样的结果
// 所以即使nums中有负数，也可以把负数直接变成正数，也不会影响结果
// 思考2:
// 如果nums都是非负数，并且所有数的累加和是sum
// 那么如果target>sum，很明显没有任何方法可以达到target，可以直接返回0
// 思考3:
// nums内部的数组，不管怎么+和-，最终的结果都一定不会改变奇偶性
// 所以，如果所有数的累加和是sum，并且与target的奇偶性不一样
// 那么没有任何方法可以达到target，可以直接返回0
// 思考4(最重要):
// 比如说给定一个数组, nums = [1, 2, 3, 4, 5] 并且 target = 3
// 其中一个方案是 : +1 -2 +3 -4 +5 = 3
// 该方案中取了正的集合为A = {1，3，5}
// 该方案中取了负的集合为B = {2，4}
// 所以任何一种方案，都一定有 sum(A) - sum(B) = target
// 现在我们来处理一下这个等式，把左右两边都加上sum(A) + sum(B)，那么就会变成如下：
// sum(A) - sum(B) + sum(A) + sum(B) = target + sum(A) + sum(B)
// 2 * sum(A) = target + 数组所有数的累加和
// sum(A) = (target + 数组所有数的累加和) / 2
// 也就是说，任何一个集合，只要累加和是(target + 数组所有数的累加和) / 2
// 那么就一定对应一种target的方式
// 比如非负数组nums，target = 1, nums所有数累加和是11
// 求有多少方法组成1，其实就是求，有多少种子集累加和达到6的方法，(1+11)/2=6
// 因为，子集累加和6 - 另一半的子集累加和5 = 1(target)
// 所以有多少个累加和为6的不同集合，就代表有多少个target==1的表达式数量
// 至此已经转化为01背包问题了
#include <bits/stdc++.h>
using namespace std;

// 求子集和为 t 的方案数（01背包 + 空间压缩）
int subsets(vector<int>& nums, int t) {
    if (t < 0) return 0;

    vector<int> dp(t + 1, 0);
    dp[0] = 1;//这里0的含义是，容量为0，target为0，凑出的方法就是空集1
    // 求非负数组nums有多少个子序列累加和是t
	// 01背包问题(子集累加和严格是t) + 空间压缩
	// dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]
    // 为什么是这个转移，首先我们要找的是方法，
    // dp参数的含义还是不变，当我们来到i，我们可以选，也可以不选
    //当前数字，然后dp数组值的含义就是这两种方法的累计，所以要加起来
    for (int num : nums) {
        for (int j = t; j >= num; --j) {
            dp[j] += dp[j - num];
        }
    }
    return dp[t];
}

// 主函数：目标和
int findTargetSumWays(vector<int>& nums, int target) {
    int sum = 0;
    for (int n : nums) {
        sum += abs(n);  // ⭐ 保证兼容负数情况
    }

    // 剪枝1：target 不可能达到
    if (sum < abs(target)) return 0;

    // 剪枝2：奇偶性不同
    if ((sum + target) % 2 != 0) return 0;

    int t = (sum + target) / 2;
    return subsets(nums, t);
}

int main() {
    vector<int> nums = {1, 1, 1, 1, 1};
    int target = 3;

    cout << findTargetSumWays(nums, target) << endl; // 输出 5
    return 0;
}