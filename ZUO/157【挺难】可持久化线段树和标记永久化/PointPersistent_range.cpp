// 单点修改的可持久化线段树模版题2，C++版
// 给定一个长度为n的数组arr，下标1~n，一共有m条查询
// 每条查询 l r k : 打印arr[l..r]中第k小的数字
// 1 <= n、m <= 2 * 10^5
// 0 <= arr[i] <= 10^9
// 测试链接 : https://www.luogu.com.cn/problem/P3834
/*
Author: yangka
Date: 2026-03-24 14:39:52
*/
//经典题，查询数组一段范围上的第k小
//流程是，来到一个下标i，建立一个版本的线段树，范围是1-i
//排名就是有多少种数字，比如10个数字，那么来到一个下标
//就简历1-10名的线段树单位是1-i
//找到k大的思路是，比较不同版本的线段树，比如查找13-27版本的线段树排名10的数字
//假设10个数字，我们比较1-12范围内排名1-5有几个数字，假设2个
//再比较1-27范围内排名1-5有几个数字，假设6个，不够，所以我们需要向右侧递归
//去找排名6-10的数字
#include <bits/stdc++.h>
using namespace std;
const int MAXN = 200001;
const int MAXT = MAXN * 22;
int n,m,s;
int arr[MAXN],sorted[MAXN],root[MAXN];
int ls[MAXT],rs[MAXT],siz[MAXT],cnt;

int kth(int num){
    int l = 0,r = s+1,mid;
    while(l+1<r){
        mid = (l+r)>>1;
        if(sorted[mid]>=num) r = mid;
        else l = mid;
    }
    return r;
}
//这里只维持一个siz数组，ls和rs是为了找到下标
int build(int l,int r){
    int rt = ++cnt;
    siz[rt] = 0;
    if(l<r){
        int mid = (l+r)>>1;
        ls[rt] = build(l,mid);
        rs[rt] = build(mid+1,r);
    }
    return rt;
}
//这里只是不同的写法，你也可以写l==r的时候
//只有来到了才需要建立，不来到就不需要建立
int insert(int jobi,int l,int r,int i){
    int rt = ++cnt;
    ls[rt] = ls[i];
    rs[rt] = rs[i];
    siz[rt] = siz[i] + 1;
    if(l<r){
        int mid = (l+r)>>1;
        if(jobi<= mid) ls[rt] = insert(jobi,l,mid,ls[rt]);
        else rs[rt] = insert(jobi,mid+1,r,rs[rt]);
    }
    return rt;
}
//刚开始一直觉得怪怪的，不太懂为什么建立1-5排名，1-5排名啥意思
//其实这个1-5不是1-5有多少数字，是真的排名，就是统计1-i，有多少数字在
//去重排序1-5范围内
int query(int jobk,int l,int r,int u,int v){
    if(l==r) return l;
    int lsize = siz[ls[v]] - siz[ls[u]];
    int mid = (l+r)>>1;
    if(lsize>=jobk) return query(jobk,l,mid,ls[u],ls[v]);
    else return query(jobk-lsize,mid+1,r,rs[u],rs[v]);

}
void prepare(){
    for(int i=1;i<=n;i++){
        sorted[i] = arr[i];
    }
    sort(sorted+1,sorted+n+1);
    s = 1;
    for(int i=2;i<=n;i++){
        if(sorted[s]!=sorted[i]){
            sorted[++s] = sorted[i];
        }
    }
    root[0] = build(1,s);
    //开始插入，每次都要建立新版本的线段树，建立在之前版本的
    //上面我们已经建立的0版本的
    for(int i=1,x;i<=n;i++){
        x = kth(arr[i]);
        root[i] = insert(x,1,s,root[i-1]);
    }
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin>>n>>m;
    for(int i=1;i<=n;i++){
        cin>>arr[i];
    }
    prepare();
    for(int i=1,l,r,k,rank;i<=m;i++){
        cin>>l>>r>>k;
        rank = query(k,1,s,root[l-1],root[r]);
        cout<<sorted[rank]<<"\n";
    }
    

    return 0;
}