// 标记永久化，范围增加 + 查询累加和，C++版
// 给定一个长度为n的数组arr，下标1~n，一共有m条操作，操作类型如下
// 1 x y k : 将区间[x, y]每个数加上k
// 2 x y   : 打印区间[x, y]的累加和
// 这就是普通线段树，请用标记永久化的方式实现
// 测试链接 : https://www.luogu.com.cn/problem/P3372
// 可持久化线段树：标记永久化（核心笔记）

// 一、概念
// - 懒标记不下传，只作用在当前区间
// - 上下层标记互不影响
// - 查询时沿路径累加所有标记

// 二、核心思想
// - 不 push down
// - 标记只保存在节点上
// - 查询时自顶向下累加标记

// 三、关键性质
// - 标记永久化 ≠ 标记不变
// - 而是不同层标记彼此独立

// 四、适用条件（必须满足）
// - 修改和查询具有“可叠加性”
//   例：
//   - 区间加 + 区间和
//   - 区间加 + 单点查询

// 五、不适用情况
// - 区间赋值 / 覆盖
// - 区间 max / min
// （这些不具备可叠加性）

// 六、优势
// - 不需要 push down
// - 查询不新建节点
// - 空间复杂度更低

// 七、复杂度
// - 每次修改：O(log n)
// - 查询：O(log n)
// - 总空间：O(n * log n)

// 八、对比
// 普通可持久化 + lazy：
// - 通用，但空间大

// 标记永久化：
// - 限制场景，但更省空间（推荐）
//来到一个节点根据加减调整区间和，然后继续向下
//如果来到一个区间把他的任务范围保住了，标记就在这里了
/*
Author: yangka
Date: 2026-03-24 16:42:42
*/

#include <bits/stdc++.h>
using namespace std;
const int MAXN = 100001;

using ll  = long long;
ll arr[MAXN],sum[MAXN<<2],addTag[MAXN<<2];

void up(int i){
    sum[i] = sum[i<<1] + sum[i<<1|1];
}
void build(int l,int r,int i){
    if(l==r) sum[i] = arr[l];
    else{
        int mid = (l+r)>>1;
        build(l,mid,i<<1);
        build(mid+1,r,i<<1|1);
        up(i);
    }
    addTag[i] = 0;
}

void add(int jobl,int jobr,ll jobv,int l,int r,int i){
    int a = max(jobl,l),b = min(jobr,r);
    sum[i]+=jobv*(b-a+1);
    if(jobl<=l && jobr>=r) addTag[i]+=jobv;
    else{
        int mid = (l+r)>>1;
        if(jobl<=mid) add(jobl,jobr,jobv,l,mid,i<<1);
        if(jobr>mid) add(jobl,jobr,jobv,mid+1,r,i<<1|1);
    }
}
ll query(int jobl,int jobr,ll addHistory,int l,int r,int i){
    if(jobl<=l && jobr>=r){
        return sum[i] + addHistory * (r - l + 1);
    }
    int mid = (l+r)>>1;
    ll ans = 0;
    if(jobl<=mid) ans+=query(jobl,jobr,addHistory+addTag[i],l,mid,i<<1);
    if(jobr>mid) ans+=query(jobl,jobr,addHistory+addTag[i],mid+1,r,i<<1|1);
    return ans;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m;
    cin>>n>>m;
    for(int i=1;i<=n;i++){
        cin>>arr[i];
    }
    build(1,n,1);
    int op,jobl,jobr;
    ll jobv;
    for(int i=1;i<=m;i++){
        cin>>op;
        if(op==1){
            cin>>jobl>>jobr>>jobv;
            add(jobl,jobr,jobv,1,n,1);
        }else{
            cin >> jobl >> jobr;
            cout << query(jobl, jobr, 0, 1, n, 1) << "\n";
        }
    }
    

    return 0;
}