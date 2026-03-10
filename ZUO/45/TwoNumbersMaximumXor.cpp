
// 数组中两个数的最大异或值
// 给你一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0<=i<=j<=n
// 1 <= nums.length <= 2 * 10^5
// 0 <= nums[i] <= 2^31 - 1
// 测试链接 : https://leetcode.cn/problems/maximum-xor-of-two-numbers-in-an-array/
//思路就是，数组建立前缀树，注意，需要保持每个数"位数"一致
//比如数组最大数二进制表示为1110010,其他数可能是1101，我们在将其他数字
//插入前缀树时候，需要调整为0001101，保持一致，
//然后我们在查询的时候，来到一个数字，哪怕他的二进制位数不到最大数字的二进制位数
//我们需要假设他有这么高的位数，只不过这一位是0，然后逐渐降低


#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    static const int MAXN = 3000001;
    int tree[MAXN][2],cnt,high;

    void build(vector<int>& nums){
        cnt = 1;
        int mx = 0;
        for(int& num:nums){
            mx = max(num,mx);
        }
        if(mx==0) high = 0;
        else high = 31 - __builtin_clz(mx);
        for(int num:nums){
            insert(num);
        }
    }
    void insert(int num){
        int cur = 1;
        for(int i=high;i>=0;i--){
            int path = (num>>i)&1;
            if(tree[cur][path]==0){
                tree[cur][path] = ++cnt;
            }
            cur = tree[cur][path];
        }
    }
    int f(int num){
        int cur = 1;
        int ans = 0;
        for(int i=high;i>=0;i--){
            int status = (num>>i)&1;
            int want = status^1;
            if(tree[cur][want]==0){
                want^=1;
            }
            cur = tree[cur][want];
            ans|=(status^want)<<i;
        }
        return ans;
    }
    void clear(){
        for(int i=1;i<=cnt;i++){
            tree[i][0] = tree[i][1] = 0;
        }
    }

    int findMaximumXOR(vector<int>& nums) {
        build(nums);
        int ans = 0;
        for(int num:nums){
            ans = max(ans,f(num));
        }
        clear();
        return ans;
    }
    //哈希表做法
    int findMaximumXOR1(vector<int>& nums) {
        
    }
};