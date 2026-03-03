#include<bits/stdc++.h>
using namespace std;

const int MAXN = 50001;
const int BIT = 30;

// 每个线段树节点维护一个线性基
int basis_tree[MAXN<<2][BIT+1];
// 查询时临时使用的线性基
int basis[BIT+1];

bool insert(int* b,int num){
    for(int i=BIT;i>=0;i--){
        if((num>>i)&1){
            if(b[i]==0){
                b[i]=num;
                return true;
            }
            num^=b[i];
        }
    }
    return false;
}

void add(int pos,int val,int l,int r,int i){
    insert(basis_tree[i],val);
    if(l==r) return;
    int mid=(l+r)>>1;
    if(pos<=mid){
        add(pos,val,l,mid,i<<1);
    }else{
        add(pos,val,mid+1,r,i<<1|1);
    }
}

void merge(int jobl, int jobr, int l, int r, int i){
    if(jobl<=l && r<=jobr){
        for(int j=BIT;j>=0;j--){
            if(basis_tree[i][j]!=0){
                insert(basis,basis_tree[i][j]);
            }
        }
    }else{
        int mid=(l+r)>>1;
        if(jobl<=mid){
            merge(jobl,jobr,l,mid,i<<1);
        }
        if(jobr>mid){
            merge(jobl,jobr,mid+1,r,i<<1|1);
        }
    }
}
int query(int jobl,int jobr,int m){
    memset(basis,0,sizeof(basis));
    merge(jobl,jobr,1,m,1);
    int ans = 0;
    for(int i=BIT;i>=0;i--){
        ans = max(ans,ans^basis[i]);
    }
    return ans;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n,m;
    cin>>n>>m;
    while(n--){
        int op;
        cin>>op;
        if(op==1){
            int pos,val;
            cin>>pos>>val;
            add(pos,val,1,m,1);
        }else{
            int l,r;
            cin>>l>>r;
            cout<<query(l,r,m)<<'\n';
        }
    }
    return 0;
}