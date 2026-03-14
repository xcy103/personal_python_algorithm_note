//这道题暴露的问题，括号优先级，zero的处理
//c++内置取位数的函数，以及第k异或和如果取到
//犯毛病，最小的异或和是从main_row - 1 开始的
#include<bits/stdc++.h>
using namespace std;
using ll = long long;

const int BIT = 50;
const int MAXN = 100005;
ll arr[MAXN];
int n,k,m,query[MAXN];

void prepare(){
    for(int i=0;i<MAXN;i++){
        arr[i] = 0;
        query[i] = 0;
    }
}

int gauss(){
    int row = 0;
    for(int i=BIT;i>=0;i--){
        for(int j=row;j<n;j++){
            if((arr[j]>>i)&1LL){
                swap(arr[j],arr[row]);
                break;
            }
        }
        if((arr[row]>>i&1LL)==0) continue;

        for(int j=0;j<n;j++){
            if(j!=row && ((arr[j]>>i)&1LL)){
                arr[j] ^= arr[row];
            }
        }
        row++;
    }
    return row;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    prepare();
    cin>>n;
    ll mx = 0;
    for(int i=0;i<n;i++) {
        cin>>arr[i];
        mx = max(mx,arr[i]);
    }
    int main_row = gauss();
    int zero = 0;
    if(main_row != (mx ? 64 - __builtin_clzll(mx) : 0)){  // FIX: 删除分号 + 处理mx=0
        zero = 1;
    } 
    cin>>m;
    for(int i=0;i<m;i++){
        ll q = 0;
        cin>>q;
        q-= zero;
        if(q>=1<<main_row){
            cout<<"-1\n";
            continue;
        }
        ll ans = 0;
        for(int j=main_row-1,k=0;j>=0;j--,k++){
            if((q>>k)&1LL){
                ans ^= arr[j];
            }
        }
        cout<<ans<<'\n';
    }
    
    return 0;
}