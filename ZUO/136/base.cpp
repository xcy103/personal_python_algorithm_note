#include<bits/stdc++.h>
using namespace std;
using ll = long long;

const int MAXN = 105;
const int BIT = 60;

ll basis[MAXN];
int len_basis;
bool zero;

//这种不保留自由元的写法挺重要的，可能有点绕，需要多看看

pair<vector<ll>,bool> solve(vector<ll> arr){
    int n = arr.size();
    for(int i = 0; i < n; i++) basis[i] = arr[i];
    
    int row = 0;
    for(int bit = BIT;bit>=0;bit--){
        int pivot = -1;
        for(int i=row;i<n;i++){
            if((basis[i]>>bit)&1){
                pivot = i;
                break;
            }
        }
        if(pivot==-1) continue;

        swap(basis[row],basis[pivot]);

        for(int i=0;i<n;i++){
            if(i!=row && ((basis[i]>>bit)&1)){
                basis[i]^=basis[row];
            }
        }
        row++;
    }
    len_basis = row;
    zero = (len_basis!=n);
    vector<ll> ans;
    for(int i = 0; i < len_basis; i++) ans.push_back(basis[i]);
    return {ans,zero};

}