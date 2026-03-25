// 范围修改的可持久化线段树，经典的方式，C++版
// 给定一个长度为n的数组arr，下标1~n，时间戳t=0，arr认为是0版本的数组
// 一共有m条操作，每条操作为如下四种类型中的一种
// C x y z : 当前时间戳t版本的数组，[x..y]范围每个数字增加z，得到t+1版本数组，并且t++
// Q x y   : 当前时间戳t版本的数组，打印[x..y]范围累加和
// H x y z : z版本的数组，打印[x..y]范围的累加和
// B x     : 当前时间戳t设置成x
// 1 <= n、m <= 10^5
// -10^9 <= arr[i] <= +10^9
// 测试链接 : https://www.luogu.com.cn/problem/SP11470
// 测试链接 : https://www.spoj.com/problems/TTM
// 可持久化线段树 和 标记永久化（范围修改）

// 一、范围修改的可持久化线段树（经典做法）

// 1. 范围修改需要懒标记（lazy tag）
// 2. 思路类似单点修改的可持久化线段树
// 3. 每访问一个节点，都新建节点，并复制旧节点信息（路径复制）
// 4. 懒标记下传（push down）时：
//    - 左右子节点都需要新建
//    - 子节点接收懒标记
//    - 原节点保持不变（保证历史版本）

// 二、复杂度分析

// 1. 每次修改：
//    - 新建 O(log n) 个节点
// 2. 查询操作：
//    - 若涉及 push down，也会新建节点
// 3. 若有 n 次修改，m 次查询：
//    - 总空间复杂度：
//      O(n * 4 + n * log n + m * log n)

// 三、重要结论

// - 只要发生懒标记下传，就必须新建节点
// - 因此范围修改的可持久化线段树，空间开销较大
// 任何的可持久化线段树都可以用经典的方式

// 四、优化：标记永久化（tag 永久化）

// 适用场景：
// - 区间加
// - 查询区间和 / 点值

// 核心思想：
// - 不下传懒标记
// - 查询时累加路径上的所有标记

// 优点：
// - 不需要 push down
// - 节点创建更少
// - 显著降低空间复杂度

// 五、总结

// 普通可持久化 + lazy：
// - 通用
// - 空间大

// 标记永久化：
// - 适用于 区间加 + 查询
// - 空间更优（推荐）
/*
Author: yangka
Date: 2026-03-24 15:50:12
*/

#include <bits/stdc++.h>
using namespace std;
const int MAXN = 100001;
const int MAXT = MAXN * 70;
using ll = long long;
int n,m,t = 0;
int arr[MAXN],root[MAXN],ls[MAXT],rs[MAXT],cnt;
ll sum[MAXT],add[MAXT];

int clone(int i){
    int rt = ++cnt;
    ls[rt] = ls[i];
    rs[rt] = rs[i];
    sum[rt] = sum[i];
    add[rt] = add[i];
    return rt;
}

void up(int i){
    sum[i] = sum[ls[i]] + sum[rs[i]];
}
void lazy(int i,ll v,int n){
    sum[i]+=v*n;
    add[i]+=v;
}
//有点不懂
//这个就是down直接抄原来节点的信息，抄一份
void down(int i,int ln,int rn){
    if(add[i]){
        ls[i] = clone(ls[i]);
        rs[i] = clone(rs[i]);
        lazy(ls[i],add[i],ln);
        lazy(rs[i],add[i],rn);
        add[i] = 0;
    }
}
int build(int l,int r){
    int rt = ++cnt;
    add[rt] = 0;
    if(l==r) sum[rt] = arr[l];
    else{
        int mid = (l+r)>>1;
        ls[rt] = build(l,mid);
        rs[rt] = build(mid+1,r);
        up(rt);
    }
    return rt;
}
int addRange(int jobl,int jobr,ll jobv,int l,int r,int i){
    int rt = clone(i);
    if(jobl<=l && jobr>=r) lazy(rt,jobv,r-l+1);
    else{
        int mid = (l+r)>>1;
        down(rt,mid-l+1,r-mid);
        if(jobl<=mid){
            ls[rt] = addRange(jobl,jobr,jobv,l,mid,ls[rt]);
        }
        if(jobr>mid){
            rs[rt] = addRange(jobl,jobr,jobv,mid+1,r,rs[rt]);
        }
        up(rt);
    }
    return rt;
}
ll query(int jobl,int jobr,int l,int r,int i){
    if(jobl<=l && jobr>=r) return sum[i];
    int mid = (l+r)>>1;
    down(i,mid-l+1,r-mid);
    ll ans = 0;
    if(jobl<=mid) ans+=query(jobl,jobr,l,mid,ls[i]);
    if(jobr>mid) ans+=query(jobl,jobr,mid+1,r,rs[i]);
    return ans;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin>>n>>m;
    for(int i=1;i<=n;i++) cin>>arr[i];

    root[0] = build(1,n);
    string op;
    int x,y,z;
    for(int i=1;i<=m;i++){
        cin>>op;
        if(op=="C"){
            cin>>x>>y>>z;
            root[t+1] = addRange(x,y,z,1,n,root[t]);
            t++;
        }else if(op=="Q"){
            cin>>x>>y;
            cout<<query(x,y,1,n,root[t])<<"\n";
        }else if(op=="H"){
            cin>>x>>y>>z;
            cout << query(x, y, 1, n, root[z]) << "\n";
        }else if(op=="B"){
            cin>>x;
            t = x;
        }

    }
    

    return 0;
}