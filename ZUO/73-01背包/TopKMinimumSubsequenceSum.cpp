// 非负数组前k个最小的子序列累加和
// 给定一个数组nums，含有n个数字，都是非负数
// 给定一个正数k，返回所有子序列中累加和最小的前k个累加和
// 子序列是包含空集的
// 1 <= n <= 10^5
// 1 <= nums[i] <= 10^6
// 1 <= k <= 10^5
// 注意这个数据量，用01背包的解法是不行的，时间复杂度太高了
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;
using ll = long long;
vector<int> topKSum3(vector<int>& nums, int k) {
    sort(nums.begin(),nums.end());

    using Node = pair<int ,ll>;
    priority_queue<Node, vector<Node>, greater<Node>> heap;

    heap.push({nums[0],0});

    vector<int> ans(k);
    ans[0] = 0;

    for(int i=1;i<k;i++){
        auto [sum,right] = heap.top();
        heap.pop();
        ans[i] = (int)sum;
        if (right+1<nums.size()){
            heap.push({sum-nums[right]+nums[right+1],right+1});
            heap.push({sum+nums[right+1],right+1});
        }
    }
    return ans;
}