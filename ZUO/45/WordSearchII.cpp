// 在二维字符数组中搜索可能的单词
// 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words
// 返回所有二维网格上的单词。单词必须按照字母顺序，通过 相邻的单元格 内的字母构成
// 其中“相邻”单元格是那些水平相邻或垂直相邻的单元格
// 同一个单元格内的字母在一个单词中不允许被重复使用
// 1 <= m, n <= 12
// 1 <= words.length <= 3 * 10^4
// 1 <= words[i].length <= 10
// 测试链接 : https://leetcode.cn/problems/word-search-ii/
//这道题trie的作用就是，建立前缀树所有要收集的单词
//1.来到一个位置看有没有必要展开，2. 如果这个位置以及以后的单词收集过
//p就--，下次来到就i可以不用沿着这个路径展开收集了
#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    static const int MN = 10001;
    int tree[MN][26],p[MN],cnt,n,m;
    string e[MN];
    vector<string> ans;

    void build(vector<string>& words){
        cnt = 1;
        for(auto& word:words){
            int cur = 1;
            p[cur]++;
            for(char ch:word){
                int path = ch-'a';
                if(tree[cur][path]==0){
                    tree[cur][path] = ++cnt;
                }
                cur = tree[cur][path];
                p[cur]++;
            }
            e[cur] = word;
        }
    }

    int dfs(vector<vector<char>>& board,int i,int j,int t){
        if(i<0||j<0||i==m||j==n||board[i][j]=='#') return 0;

        char ch = board[i][j];
        int path = ch-'a';
        t = tree[t][path];
        if(t==0||p[t]==0) return 0;

        int fix = 0;
        if(e[t]!=""){
            fix++;
            ans.push_back(e[t]);
            e[t] = "";
        }
        board[i][j] = '#';
        fix += dfs(board,i-1,j,t);
        fix += dfs(board,i+1,j,t);
        fix += dfs(board,i,j-1,t);
        fix += dfs(board,i,j+1,t);
        board[i][j] = ch;
        p[t]-=fix;
        return fix;
    }
    void clear(){
        for(int i=1;i<=cnt;i++){
            memset(tree[i],0,sizeof(tree[i]));
            p[i] = 0;
            e[i] = "";
        }
    }
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        build(words);
        m = board.size();
        n = board[0].size();

        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                dfs(board,i,j,1);
            }
        }
        return ans;
    }
};