#include<vector>
#include<algorithm>
#include<queue>
// 找出数组的第K大和
// 给定一个数组nums和正数k
// 可以选择数组的任何子序列并对其元素求和
// 希望找到第k大的子序列和，子序列和允许出现重复
// 空子序列的和视作0，数组中的值可正、可负、可0
// 测试链接 : https://leetcode.cn/problems/find-the-k-sum-of-an-array/description/
//
// 转化逻辑如下 : 
// 1，先把所有正数加起来，得到sum，这是nums第1大子序列和
// 2，nums第2大子序列和，要么sum中去掉一个最小的正数，要么sum + (选剩下的非正数字，拼出最大的累加和)
// 3，nums第2大子序列和 = (sum - 最小的正数) 或者 (sum - 选剩下的非正数字，拼出最小的绝对值)
// 4，原始数组记为nums，把每个数转成绝对值的数组记为a
// 5，nums第1大子序列和 = sum = sum - 0，其中0表示数组a取空集的累加和，认为是a的第1小子序列和
// 6，nums第1大子序列和 = sum - a的第1小子序列和
// 7，nums第2大子序列和 = sum - a的第2小子序列和
// 8，nums第k大子序列和 = sum - a的第k小子序列和
// 9，求a的第k小子序列和即可，注意，a的第1小子序列和，是空集的情况

using ll = long long;
class Solution {
public:
    long long kSum(vector<int>& nums, int k) {
        int n = nums.size();
        long long sum = 0;

        // 1. 正数累加，负数取绝对值
        for (int& x : nums) {
            if (x > 0) sum += x;
            else x = -x;
        }

        sort(nums.begin(), nums.end());

        using Node = pair<long long, int>; // (当前子序列和, idx)
        priority_queue<Node, vector<Node>, greater<Node>> heap;

        // 空集：idx = -1, sum = 0
        heap.push({0, -1});

        // 弹出前 k-1 小
        for (int i = 1; i < k; i++) {
            auto [val, idx] = heap.top();
            heap.pop();

            if (idx + 1 < n) {
                // 新加入 nums[idx+1]
                heap.push({val + nums[idx + 1], idx + 1});

                // 替换 nums[idx] -> nums[idx+1]
                if (idx >= 0) {
                    heap.push({val - nums[idx] + nums[idx + 1], idx + 1});
                }
            }
        }

        // 第 k 小子序列和
        return sum - heap.top().first;
    }
};