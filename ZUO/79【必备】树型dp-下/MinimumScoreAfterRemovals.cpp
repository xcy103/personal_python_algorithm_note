// 从树中删除边的最小分数
// 存在一棵无向连通树，树中有编号从0到n-1的n个节点，以及n-1条边
// 给你一个下标从0开始的整数数组nums长度为n，其中nums[i]表示第i个节点的值
// 另给你一个二维整数数组edges长度为n-1
// 其中 edges[i] = [ai, bi] 表示树中存在一条位于节点 ai 和 bi 之间的边
// 删除树中两条不同的边以形成三个连通组件，对于一种删除边方案，定义如下步骤以计算其分数：
// 分别获取三个组件每个组件中所有节点值的异或值
// 最大 异或值和 最小 异或值的 差值 就是这种删除边方案的分数
// 返回可能的最小分数
// 测试链接 : https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/

class Solution {
public:
    static const int MAXN = 1001;
    int dfn[MAXN],xsum[MAXN],sz[MAXN],cntd;

    void f(vector<int>& nums,vector<vector<int>>& g,int u){
        int i = ++cntd;
        dfn[u] = i;
        sz[i] = 1;
        xsum[i] = nums[u];
        for(int& v:g[u]){
            if(dfn[v]==0){
                f(nums,g,v);
                sz[i]+=sz[dfn[v]];
                xsum[i]^=xsum[dfn[v]];
            }
        }
    }
    int minimumScore(vector<int>& nums, vector<vector<int>>& edges) {
        int n = nums.size();
        vector<vector<int>> g(n);
        for(auto& e:edges){
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        memset(dfn,0,sizeof(dfn));
        cntd = 0;
        f(nums,g,0);
        int m = edges.size();
        int ans = INT_MAX;
        for(int i=0;i<m;i++){
            int a = max(dfn[edges[i][0]],dfn[edges[i][1]]);
            for(int j = i+1;j<m;j++){
                int b = max(dfn[edges[j][0]],dfn[edges[j][1]]);
                
                int sml = min(a,b);
                int big = max(a,b);
                int s1 = xsum[big];
                int s2,s3;
                if(big<sml+sz[sml]){
                    //在里面
                    s2 = xsum[sml]^s1;
                    s3 = xsum[1]^xsum[sml];
                }else{
                    //互不相干
                    s2 = xsum[sml];
                    s3 = xsum[1]^s1^s2;
                }
                int mx = max({s1,s2,s3});
                int mn = min({s1,s2,s3});
                ans = min(ans,mx-mn);
            }
        }
        return ans;
    }
};