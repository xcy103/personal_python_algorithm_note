// 动态开点线段树
// 一共有n个位置，编号从1~n，一开始所有位置的值为0
// 实现如下两个操作，一共会调用m次
// 操作 1 l r v : 把l~r范围的每个数增加v
// 操作 2 l r   : 返回l~r范围的累加和
// 1 <= n <= 10^9
// 1 <= m <= 10^3
// 测试链接 : https://www.luogu.com.cn/problem/P2781
/*
Author: yangka
Date: 2026-03-20 23:47:03
*/

#include <bits/stdc++.h>
using namespace std;
const int LIMIT = 80001;

using ll  = long long;
int cnt,n,m;
// 动态开点
int le[LIMIT],ri[LIMIT];
// 线段树信息
ll sum[LIMIT],add[LIMIT];

void up(int i){
    sum[i] = sum[le[i]] + sum[ri[i]];
}
void lazy(int i,ll v,int n){
    sum[i] += v*n;
    add[i] += v;
}
void down(int i,int ln,int rn){
    if(add[i]){
        if(le[i]==0) le[i] = ++cnt;
        if(ri[i]==0) ri[i] = ++cnt;
        lazy(le[i], add[i], ln);
        lazy(ri[i], add[i], rn);
        add[i] = 0;
    }
}
void range(int jobl,int jobr,int jobv,int l,int r,int i){
    if(jobl<=l && jobr>=r){
        lazy(i,jobv,r-l+1);
    }else{
        int mid = (r+l)>>1;
        down(i,mid-l+1,r-mid);
        if(jobl<=mid){
            if(le[i]==0) le[i] = ++cnt;
            range(jobl,jobr,jobv,l,mid,le[i]);
        }
        if(jobr>mid){
            if(ri[i]==0) ri[i] = ++cnt;
            range(jobl,jobr,jobv,mid+1,r,ri[i]);
        }
        up(i);
    }
}
ll query(int jobl,int jobr,int l,int r,int i){
    if(jobl<=l && jobr>=r) return sum[i];
    int mid = (l+r)>>1;
    down(i,mid-l+1,r-mid);
    ll ans = 0;
    // 发现左侧申请过空间才有必要去查询
	// 如果左侧从来没有申请过空间那查询结果就是0
    if(jobl<=mid && le[i]) ans+=query(jobl,jobr,l,mid,le[i]);
    // 发现右侧申请过空间才有必要去查询
	// 如果右侧从来没有申请过空间那查询结果就是0
    if(jobr>mid && ri[i]) ans+=query(jobl,jobr,mid+1,r,ri[i]);
    return ans;
}
// 清空（多组数据才用）
void clear_all() {
    for (int i = 1; i <= cnt; i++) {
        le[i] = ri[i] = 0;
        sum[i] = add[i] = 0;
    }
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin>>n>>m;
    cnt = 1;
    int op,l,r;
    ll v;
    for(int i=1;i<=m;i++){
        cin>>op;
        if(op==1){
            cin>>l>>r>>v;
            range(l,r,v,1,n,1);
        }else{
            cin>>l>>r;
            cout << query(l, r, 1, n, 1) << '\n';
        }
    }

    return 0;
}