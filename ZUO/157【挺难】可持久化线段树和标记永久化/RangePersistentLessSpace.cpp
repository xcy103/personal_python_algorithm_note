// 范围修改的可持久化线段树，标记永久化减少空间占用，C++版
// 给定一个长度为n的数组arr，下标1~n，时间戳t=0，arr认为是0版本的数组
// 一共有m条查询，每条查询为如下四种类型中的一种
// C x y z : 当前时间戳t版本的数组，[x..y]范围每个数字增加z，得到t+1版本数组，并且t++
// Q x y   : 当前时间戳t版本的数组，打印[x..y]范围累加和
// H x y z : z版本的数组，打印[x..y]范围的累加和
// B x     : 当前时间戳t设置成x
// 1 <= n、m <= 10^5
// -10^9 <= arr[i] <= +10^9
// 测试链接 : https://acm.hdu.edu.cn/showproblem.php?pid=4348
/*
Author: yangka
Date: 2026-03-24 17:01:16
*/

#include <bits/stdc++.h>
using namespace std;
const int MAXN = 100001;
const int MAXT = MAXN * 25;
using ll  = long long;
int n,m,t;
ll arr[MAXN],sum[MAXT],addTag[MAXT];
int root[MAXN],ls[MAXT],rs[MAXT],cnt;

int build(int l,int r){
    int rt = ++cnt;
    addTag[rt] = 0;
    if(l==r) sum[rt] = arr[l];
    else{
        int mid = (l+r)>>1;
        ls[rt] = build(l,mid);
        rs[rt] = build(mid+1,r);
        sum[rt] = sum[ls[rt]] + sum[rs[rt]];
    }
    return rt;
}
int add(int jobl,int jobr,ll jobv,int l,int r,int i){
    int rt = ++cnt,a = max(jobl,l),b = min(jobr,r);
    ls[rt] = ls[i];
    rs[rt] = rs[i];
    sum[rt] = sum[i] + jobv*(b-a+1);
    addTag[rt] = addTag[i];
    if(jobl<=l && jobr>=r) addTag[rt]+=jobv;
    else{
        int mid = (l+r)>>1;
        if(jobl<=mid) ls[rt] = add(jobl,jobr,jobv,l,mid,ls[rt]);
        if(jobr>mid) rs[rt] = add(jobl,jobr,jobv,mid+1,r,rs[rt]);
    }
    return rt;
}
ll query(int jobl,int jobr,ll pre,int l,int r,int i){
    if(jobl<=l && jobr>=r) return sum[i] + pre*(r-l+1);
    int mid = (l+r)>>1;
    ll ans = 0;
    if(jobl<=mid) ans+=query(jobl,jobr,pre+addTag[i],l,mid,ls[i]);
    if(jobr>mid) ans+=query(jobl,jobr,pre+addTag[i],mid+1,r,rs[i]);
    return ans;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin>>n>>m;
    for(int i=1;i<=n;i++) cin>>arr[i];
    root[0] = build(1,n);
    char op;
    int x,y;
    ll z;
    for(int i=1;i<=m;i++){
        cin>>op;
        if(op=='C'){
            cin>>x>>y>>z;
            root[t+1] = add(x,y,z,1,n,root[t]);
            t++;
        }else if(op=='Q'){
            cin>>x>>y;
            cout<<query(x,y,0,1,n,root[t])<<"\n";
        }else if(op=='H'){
            cin>>x>>y>>z;
            cout<<query(x,y,0,1,n,root[z])<<"\n";
        }else{
            cin>>x;
            t = x;
        }
    }
    

    return 0;
}