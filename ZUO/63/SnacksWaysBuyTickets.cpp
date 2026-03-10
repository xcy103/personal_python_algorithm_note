// #双向广搜
// #其实就是折半搜索。。单词接龙1这道题算是用双向广搜
// #
#include<bits/stdc++.h>
using namespace std;
using ll = long long;
const int MAXN = 40;
const int MAXM = 1<<20;
ll arr[MAXN],lsum[MAXM],rsum[MAXM],w;

int n;
//arr[i...e]展开，不再进行往后
//s是累加和，w是背包最大容量,ans就是要填入的数组
//j就是ans数组填到了什么位置
int f(int i,int e,ll s,ll ans[],int j){
    if(s>w) return j;
    if(i==e) ans[j++] = s;
    else{
        j = f(i+1,e,s,ans,j);
        j = f(i+1,e,s+arr[i],ans,j);
    }
    return j;
}
ll compute(){
    int lsize = f(0,n>>1,0,lsum,0);
    int rsize = f(n>>1,n,0,rsum,0);

    sort(lsum,lsum+lsize);
    sort(rsum,rsum+rsize);
    ll ans = 0;
    for(int i=lsize-1,j=0;i>=0;i--){
        while (j < rsize && lsum[i] + rsum[j] <= w) j++;
        ans += j;
    }
    return ans;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin>>n>>w;
    for(int i=0;i<n;i++) cin>>arr[i];
    cout<<compute()<<endl;
}

