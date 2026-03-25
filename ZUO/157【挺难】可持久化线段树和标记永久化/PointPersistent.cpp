// 单点修改的可持久化线段树模版题1，C++版
// 给定一个长度为n的数组arr，下标1~n，原始数组认为是0号版本
// 一共有m条操作，每条操作是如下两种类型中的一种
// v 1 x y : 基于v号版本的数组，把x位置的值设置成y，生成新版本的数组
// v 2 x   : 基于v号版本的数组，打印x位置的值，生成新版本的数组和v版本一致
// 每条操作后得到的新版本数组，版本编号为操作的计数
// 1 <= n, m <= 10^6
// 测试链接 : https://www.luogu.com.cn/problem/P3919
/*
Author: yangka
Date: 2026-03-24 14:17:59
*/
//不管是操作一还是二，都会生成新的版本的数组，但是操作二是一致的

#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1000001;
const int MAXT = MAXN * 23;
// root[i] : i号版本线段树的头节点编号
// value[i] : 节点i的值信息，只有叶节点有这个信息
int n,m,arr[MAXN],root[MAXN],ls[MAXT],rs[MAXT],value[MAXT],cnt;

int build(int l,int r){
    int rt = ++cnt;
    if(l==r) value[rt] = arr[l];
    else{
        int mid = (l+r)>>1;
        ls[rt] = build(l,mid);
        rs[rt] = build(mid+1,r);
    }
    return rt;
}

int update(int jobi,int jobv,int l,int r,int i){
    //我们来到一个节点，就先复制它的值和左右孩子
    //然后看看哪个需要去往，去往的继续去修改，不去的就保留了
    //可以画个图帮助理解，
    int rt = ++cnt;
    //复制
    ls[rt] = ls[i];
    rs[rt] = rs[i];
    value[rt] = value[i];
    if(l==r) value[rt] = jobv;
    else{
        int mid = (r+l)>>1;
        if(jobi<=mid) ls[rt] = update(jobi,jobv,l,mid,ls[rt]);
        else rs[rt] = update(jobi,jobv,mid+1,r,rs[rt]);
    }
    return rt;
}

int query(int jobi,int l,int r,int i){
    if(l==r) return value[i];
    int mid = (l+r)>>1;
    if(jobi<=mid) return query(jobi,l,mid,ls[i]);
    else return query(jobi,mid+1,r,rs[i]);
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin>>n>>m;
    for(int i=1;i<=n;i++){
        cin>>arr[i];
    }
    root[0] = build(1,n);
    for(int i=1,v,op,x,y;i<=m;i++){
        cin>>v>>op>>x;
        if(op==1){
            cin>>y;
            root[i] = update(x,y,1,n,root[v]);
        }else{
            root[i] = root[v];
            cout<<query(x,1,n,root[i])<<"\n";
        }
    }

    return 0;
}