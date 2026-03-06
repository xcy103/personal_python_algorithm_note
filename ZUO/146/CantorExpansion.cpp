// 康托展开
// 数字从1到n，可以有很多排列，给出具体的一个排列，求该排列的名次，答案对 998244353 取模
// 1 <= n <= 10^6
// 测试链接 : https://www.luogu.com.cn/problem/P5367
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