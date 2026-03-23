// 康托展开
// 数字从1到n，可以有很多排列，给出具体的一个排列，求该排列的名次，答案对 998244353 取模
// 1 <= n <= 10^6
// 测试链接 : https://www.luogu.com.cn/problem/P5367
// # 康托展开（Cantor Expansion）

// 作用：
// 求一个排列在所有排列中的字典序排名（从0开始）

// 公式：
// rank = sum_{i=1..n} ( rightSmall(S[i]) * (n - i)! )

// 其中：
// rightSmall(S[i]) = 在 i 右侧比 S[i] 小的数的个数

// 注意：
// - 排名从 0 开始（不是从 1）
// - n <= 1e6 时需要预处理阶乘 + 取模
// - 常用取模：998244353

// 做法：
// 1. 预处理 factorial[]
// 2. 从左到右枚举 i
// 3. 用数据结构统计右侧比当前小的数个数
//    - 树状数组（推荐）
//    - 线段树（可行但常数大）

// 复杂度：
// O(n log n)

// 树状数组思路：
// - 初始把所有数出现次数标为1
// - 枚举 S[i]：
//     rightSmall = query(S[i]-1)
//     ans += rightSmall * fact[n-i]
//     update(S[i], -1)

// 逆康托展开（求第k个排列）：
// - 从高位到低位贪心
// - 每次确定当前位置放哪个未使用的数

// 总结：
// 康托展开 = “每一位贡献 + 阶乘权重”
#include<bits/stdc++.h>
using namespace std;
using ll = long long;

const int MAXN = 1000001;
const int MOD = 998244353;

int n,arr[MAXN],fact[MAXN],tree[MAXN];

int sum(int i){
    int ans = 0;
    while(i){
        ans = (ans + tree[i])%MOD;
        i&=(i-1);
    }
    return ans;
}
void add(int i,int v){
    while(i<=n){
        tree[i] += v;
        i+=(i&-i);
    }
}
ll compute(){
    fact[0] = 1;
    for(int i=1;i<n;i++){
        fact[i] = ((ll)fact[i-1]*i)%MOD;    
    }  
    for(int i = 1; i <= n; i++){
        add(i,1);
    }

    ll ans = 0;
    for(int i=1;i<=n;i++){
        ans = (ans+(ll)sum(arr[i]-1)*fact[n-i]%MOD)%MOD;
        add(arr[i],-1);
    }
    return (ans+1)%MOD;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin>>n;
    for(int i=1;i<=n;i++){
        cin>>arr[i];
    }
    cout<<compute()<<"\n";
    return 0;
}