//普通消元，低位插入的向量并不会让高位的基向量对应的位
//上的1消除为0，所以当我们用普通消元得到一组基向量，我们需要从高
//向低遍历得到最大xor值
#include<bits/stdc++.h>
using namespace std;
using ll = long long;
const int MAXN = 51;
const int BIT = 50;

ll arr[MAXN],basis[MAXN];
int n;

void insert_basis(ll num){
    for(int i = BIT; i >= 0; i--){
        if((num>>i)&1LL){
            if(!basis[i]){
                basis[i] = num;
                return;
            }
            num ^= basis[i];
        }
    }
    
}

ll compute(){
    for(int i=1;i<=n;i++){
        insert_basis(arr[i]);
    }
    ll ans = 0;
    for(int i=BIT;i>=0;i--){
        ans = max(ans,ans^basis[i]);
    }
    return ans;
    //return basis[BIT];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin>>n;
    for(int i=1;i<=n;i++){
        cin>>arr[i];
    }
    cout<<compute()<<"\n";
    return 0;
}