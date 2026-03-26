#  移除子树后的二叉树高度
#  给你一棵 二叉树 的根节点 root ，树中有 n 个节点
#  每个节点都可以被分配一个从 1 到 n 且互不相同的值
#  另给你一个长度为 m 的数组 queries
#  你必须在树上执行 m 个 独立 的查询，其中第 i 个查询你需要执行以下操作：
#  从树中 移除 以 queries[i] 的值作为根节点的子树
#  题目所用测试用例保证 queries[i] 不等于根节点的值
#  返回一个长度为 m 的数组 answer
#  其中 answer[i] 是执行第 i 个查询后树的高度
#  注意：
#  查询之间是独立的，所以在每个查询执行后，树会回到其初始状态
#  树的高度是从根到树中某个节点的 最长简单路径中的边数
#  测试链接 : https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#define vve vector<vector<int>>
#define ve vector<int>
#define ll long long
#define MAX 100010
ve size1(100010);
ve deep(100010);
ve maxl(100010);
ve maxr(100010);
ve dfn(100010);
class Solution {
public:
    int cnt;
    void f(TreeNode* root,int k){
        int i = ++cnt;
        dfn[root->val] = i;
        deep[i] = k;
        size1[i] = 1;
        if(root->left){
            f(root->left,k+1);
            size1[i] += size1[dfn[root->left->val]];
        }
        if(root->right){
            f(root->right,k+1);
            size1[i] += size1[dfn[root->right->val]];
        }
    }
    vector<int> treeQueries(TreeNode* root, vector<int>& queries) {
        cnt = 0;
        f(root,0);
        for(int i=1;i<=cnt;i++){
            maxl[i] = max(maxl[i-1],deep[i]);
        }
        maxr[cnt + 1] = 0;
        for(int i=cnt;i>=1;i--){
            maxr[i] = max(maxr[i+1],deep[i]);
        }
        int n = queries.size();
        ve ans(n);
        for(int i=0;i<n;i++){
            ans[i] = max(maxl[dfn[queries[i]] - 1],maxr[dfn[queries[i]] + size1[dfn[queries[i]]]]);
            
        }
        return ans;
    }
};