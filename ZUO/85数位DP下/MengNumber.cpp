//这里学到的技巧是记忆化改为挂缓存，就是每个参数对应一个维度
#include<bits/stdc++.h>
using namespace std;
using ll=long long;
const int MOD = 1000000007;

int dp[1001][11][11][2][2][2][2];

string L,R;
int n;

int dfs(int i,int pp,int p,bool is_meng,bool limit_low,bool limit_high,bool is_num){
    if(i==n){
        return is_meng?1:0;
    }
    if (dp[i][pp][p][is_meng][limit_low][limit_high][is_num] != -1) {
        return dp[i][pp][p][is_meng][limit_low][limit_high][is_num];
    }
    int lo = limit_low ? L[i] - '0' : 0;
    int hi = limit_high ? R[i] - '0' : 9;
    ll ans = 0;
    for(int d=lo;d<=hi;d++){
        bool next_limit_low = limit_low && (d == lo);
        bool next_limit_high = limit_high && (d == hi);
        if(!is_num&&d==0){
            ans = (ans + dfs(i + 1, 10, 10, false, next_limit_low, next_limit_high, false)) % MOD;
        }else{
            bool next_meng = is_meng ||  (d == p || d == pp);
            ans = (ans + dfs(i + 1, p, d, next_meng, next_limit_low, next_limit_high, true)) % MOD;
        }
    }
    return dp[i][pp][p][is_meng][limit_low][limit_high][is_num] = (int)ans;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    string l,r;
    if(!(cin>>l>>r)) return 0;

    R = r;
    n = R.size();
    L = string(n-l.size(),'0')+l;
    memset(dp,-1,sizeof(dp));
    cout<<dfs(0,10,10,false,true,true,false)<<"\n";
    return 0;
}