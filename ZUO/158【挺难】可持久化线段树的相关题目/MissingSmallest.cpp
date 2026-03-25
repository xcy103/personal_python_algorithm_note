// 区间内没有出现的最小自然数，C++版
// 给定一个长度为n的数组arr，下标1~n，一共有m条查询
// 每条查询 l r : 打印arr[l..r]内没有出现过的最小自然数，注意0是自然数
// 请用在线算法解决该问题，因为可以设计强制在线的要求，让离线算法失效
// 1 <= n、m <= 2 * 10^5
// 0 <= arr[i] <= 2 * 10^5
// 测试链接 : https://www.luogu.com.cn/problem/P4137
/*
Author: yangka
Date: 2026-03-25 15:04:39
*/

#include <bits/stdc++.h>
using namespace std;
const int MAXN = 200001;
const int MAXT = MAXN * 22;
int n,m,arr[MAXN],root[MAXN],ls[MAXT],rs[MAXT],late[MAXT],cnt;

int build(int l,int r){
    int rt = ++cnt;
    late[rt] = 0;
    if(l<r){
        int mid = (l+r)/2;
        ls[rt] = build(l,mid);
        rs[rt] = build(mid+1,r);
    }
    return rt;
}

int update(int jobi,int jobv,int l,int r,int i){
    int rt = ++cnt;
    ls[rt] = ls[i];
    rs[rt] = rs[i];
    late[rt] = late[i];
    if(l==r) late[rt] = jobv;
    else{
        int mid = (l+r)/2;
        if(jobi<=mid) ls[rt] = update(jobi,jobv,l,mid,ls[rt]);
        else rs[rt] = update(jobi,jobv,mid+1,r,rs[rt]);
        late[rt] = min(late[ls[rt]],late[rs[rt]]);
    }
    return rt;
}

int query(int pos,int l,int r,int i){
    if(l==r) return l;
    int mid = (l+r)/2;
    if(late[ls[i]]<pos) return query(pos,l,mid,ls[i]);
    else return query(pos,mid+1,r,rs[i]);
}
void prepare(){
    cnt = 0;
    root[0] = build(0,n);
    for(int i=1;i<=n;i++){
        if(arr[i]>n || arr[i]<0) root[i] = root[i-1];
        else root[i] = update(arr[i],i,0,n,root[i-1]);
    }
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin>>n>>m;
    for(int i=1;i<=n;i++) cin>>arr[i];
    prepare();
    for(int i=1,l,r;i<=m;i++){
        cin>>l>>r;
        cout << query(l, 0, n, root[r]) << "\n";
    }
    

    return 0;
}