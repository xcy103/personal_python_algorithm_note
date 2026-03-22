// 长链剖分优化动态规划模版题，C++版
// 一共有n个节点，给定n-1条边，所有节点连成一棵树，规定1号节点是头
// 规定任何点到自己的距离为0
// 定义d(u, x)，以u为头的子树中，到u的距离为x的节点数
// 对于每个点u，想知道哪个尽量小的x，能取得最大的d(u, x)值
// 打印每个点的答案x
// 1 <= n <= 10^6
// 测试链接 : https://www.luogu.com.cn/problem/CF1009F
// 测试链接 : https://codeforces.com/problemset/problem/1009/F

// 长链剖分优化树上DP

// 设 dp[u][...] 为节点 u 的动态规划表
// dp 状态与子树高度相关，可用长链剖分优化
// 可优化时间 + 空间（压缩 dp 表）
// 关键：确定每个节点 dp 的含义，以及 dp 从哪里开始存
// 长儿子 dp：父节点直接继承
// 其他儿子 dp：暴力合并
// 每条长链只遍历一次，时间复杂度 O(n)

// 实现步骤

// 找长儿子，确定节点顺序
// 先处理长儿子 → dp 直接继承
// 再处理其他儿子 → 暴力合并
// 总复杂度 O(n)
/*
Author: yangka
Date: 2026-03-21 21:14:46
*/

#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1000001;

using ll  = long long;
int n;
// 链式前向星
int head[MAXN], nxt[MAXN<<1], to[MAXN<<1], cntg;
//长剖
int len[MAXN],son[MAXN],dfn[MAXN],cntd;
//动态规划
int dp[MAXN],ansx[MAXN];

void setdp(int u,int i,int v){
    dp[dfn[u]+i] = v;
}
int getdp(int u,int i){
    return dp[dfn[u]+i];
}
void addEdge(int u, int v) {
   nxt[++cntg] = head[u];
   to[cntg] = v;
   head[u] = cntg;
}
void dfs1(int u,int f){
    for(int e = head[u],v;e;e = nxt[e]){
        v = to[e];
        if(v!=f) dfs1(v,u);
    }
    for(int e = head[u],v;e;e = nxt[e]){
        v = to[e];
        if(v!=f){
            if(son[u] == 0|| len[son[u]]<len[v]) son[u] = v;
        }
    }
    len[u] = len[son[u]] + 1;
}   
//设置dfn
void dfs2(int u,int f){
    dfn[u] = ++cntd;
    setdp(u,0,1);
    ansx[u] = 0;
    if(son[u]==0) return;
    dfs2(son[u],u);
    //注意这一循环，需要先去子节点，子节点处理完了再搞父节点的dp
    for (int e = head[u], v; e > 0; e = nxt[e]) {
        v = to[e];
        if (v != f && v != son[u]) {
            dfs2(v, u);
        }
    }
    // 注意一定要在合并其他儿子dp信息的过程中，去更新ansx
    // 千万不要，最后再遍历一遍u的dp信息，然后更新ansx
    // 因为任何for循环，都不能是长链的规模！
    // 如果for循环是长链的规模，那么u遍历下去，u的重儿子又遍历下去，长链上每个节点都遍历下去
    // 时间复杂度必然不再是O(n)，而是O(n^2)，长链剖分的优势就不存在了！
    // 所以长链信息会被u直接继承，绝对不要有任何与长链的长度等规模的循环出现！
    ansx[u] = ansx[son[u]] + 1;
    for(int e = head[u],v;e;e = nxt[e]){
        v = to[e];
        if(v!=f && v!=son[u]){
            for(int i=1;i<=len[v];i++){
                setdp(u,i,getdp(u,i)+getdp(v,i-1));
                if(getdp(u,i)>getdp(u,ansx[u]) || 
                (getdp(u,i)==getdp(u,ansx[u]) && i<ansx[u])){
                    ansx[u] = i;
                }
            }
        }
    }
    // 如果u的某个距离，获得的最大节点数为1
    // 那么u答案就是0距离，因为u到u自己的距离是0，也有1个节点了
    // 根据题目要求，返回尽量小的距离
    if(getdp(u,ansx[u])==1) ansx[u] = 0;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin>>n;
    for(int i=1,u,v;i<n;i++){
        cin>>u>>v;
        addEdge(u,v);
        addEdge(v,u);
    }
    dfs1(1,0);
    dfs2(1,1);
    for(int i=1;i<=n;i++){
        cout << ansx[i] << "\n";
    }
    

    return 0;
}