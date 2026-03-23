// 逆康托展开
// 数字从1到n，可以有很多排列，给定一个长度为n的数组s，表示具体的一个排列
// 求出这个排列的排名假设为x，打印第x+m名的排列是什么
// 1 <= n <= 10^5
// 1 <= m <= 10^15
// 题目保证s是一个由1~n数字组成的正确排列，题目保证x+m不会超过排列的总数
// 测试链接 : https://www.luogu.com.cn/problem/U72177
// # 逆康托展开（Cantor Inverse）

// 作用：
// 已知排名 k，求对应的排列（字典序第 k 个，从 0 开始）

// 核心思想：
// 用“阶乘进制”表示 k，每一位决定当前位置选第几个未使用的数

// 关键点：
// - k 不能直接取模（否则信息丢失）
// - 用阶乘进制逐位拆解 k
// - 每一位对应一个选择下标

// 做法：
// 1. 预处理 factorial[]
// 2. 准备有序集合（1~n，表示还没用的数）
// 3. 从 i = 1 到 n：
//     idx = k / (n - i)!
//     k   = k % (n - i)!
//     选择当前未使用数中的第 idx 个
//     删除该数

// 数据结构：
// - 线段树（推荐，支持第k小查询）
// - 不推荐树状数组（需要二分找第k小，稍复杂）

// 复杂度：
// O(n log n)

// 总结：
// 逆康托展开 = “用阶乘进制逐位选数”
#include<bits/stdc++.h>
using namespace std;
using ll = long long;

const int MAXN = 100001;

ll arr[MAXN],m;
int tree[MAXN<<2],n;

void build(int l,int r,int i){
    if(l==r){
        tree[i] = 1;
        return;
    }else{
        int mid = (l+r)>>1;
        build(l,mid,i<<1);
        build(mid+1,r,i<<1|1);
        tree[i] = tree[i<<1] + tree[i<<1|1];
    }
}
void update(int jobi,int jobv, int l,int r,int i){
    if(l==r){
        tree[i]+= jobv;
        return;
    }else{
        int mid = (l+r)>>1;
        if(jobi<=mid) update(jobi,jobv,l,mid,i<<1);
        else update(jobi,jobv,mid+1,r,i<<1|1);
        tree[i] = tree[i<<1] + tree[i<<1|1];
    }
}

int query(int jobl,int jobr,int l,int r,int i){
    if(jobl<=l && r<=jobr){
        return tree[i];
    }else{
        int mid = (l+r)>>1;
        int ans = 0;
        if(jobl<=mid) ans += query(jobl,jobr,l,mid,i<<1);
        if(jobr>mid) ans += query(jobl,jobr,mid+1,r,i<<1|1);
        return ans;
    }
}
// 找第k小并删除
int getAndDelete(int k,int l,int r,int i){
    if(l==r){
        tree[i]--;
        return l;
    }else{
        int mid = (l+r)>>1;
        int ans;
        if(tree[i<<1]>=k) ans = getAndDelete(k,l,mid,i<<1);
        else ans = getAndDelete(k-tree[i<<1],mid+1,r,i<<1|1);

        tree[i] = tree[i<<1] + tree[i<<1|1];
        return ans;
    }
}

void compute(){
    build(1,n,1);
    for(int i=1;i<=n;i++){
        int x = arr[i];
        if(x==1) arr[i] = 0;
        else arr[i] = query(1,x-1,1,n,1);
        update(x,-1,1,n,1);
    }
    //这一步求的是有几个数字小于它，
    //我们在线段树里用的是排名
    arr[n]+=m;
    for(int i=n;i>=1;i--){
        arr[i-1]+=arr[i]/(n-i+1);
        arr[i]%=(n-i+1);
    }
    
    build(1,n,1);
    for(int i=1;i<=n;i++){
        arr[i] = getAndDelete(arr[i]+1,1,n,1);
    }
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin>>n>>m;
    for(int i=1;i<=n;i++){
        cin>>arr[i];
    }
    compute();
    for(int i=1;i<=n;i++){
        cout<<arr[i]<<" ";
    }
    return 0;
}