//使用前缀树，不过这道题需要注意的是，相邻数字可能差值过大
//需要准成字符串后再转为多条路径，并且需要加入#隔断
#include<bits/stdc++.h>
using namespace std;
const int MAXN = 2000001;

int tree[MAXN][12],p[MAXN],e[MAXN],cnt;

void build(){
    cnt = 1;
}

int path(char c){
    if(c=='#') return 11;
    if(c=='-') return 10;
    return c-'0';
}
void insert_word(const string& word){
    int cur = 1;
    p[cur]++;
    for(char c:word){
        int nxt = path(c);
        if(tree[cur][nxt]==0){
            tree[cur][nxt] = ++cnt;
        }
        cur = tree[cur][nxt];
        p[cur]++;
    }
    e[cur]++;
}
int count(const string& word){
    int cur = 1;
    for(char c:word){
        int nxt = path(c);
        if(tree[cur][nxt]==0){
            return 0;
        }
        cur = tree[cur][nxt];
    }
    // int a =  __builtin_clz(cur);
    return p[cur];
}
void clear(){
    for(int i=1;i<=cnt;i++){
        memset(tree[i],0,sizeof(tree[i]));
        p[i] = e[i] = 0;
    }
}

int main(){
    vector<vector<int>> b;
    vector<vector<int>> a;
    build();

    string s;
    for(auto& num:a){
        s.clear();
        for(int i=1;i<num.size();i++){
            s+=to_string(num[i]-num[i-1]);
            s+='#';
        }
        insert_word(s);
    }
    vector<int> ans(b.size());
    for(int i=0;i<b.size();i++){
        s.clear();
        auto& num = b[i];
        for(int j=1;j<num.size();j++){
            s+=to_string(num[j]-num[j-1]);
            s+='#';
        }
        ans[i] = count(s);
    }
    clear();
    //return ans;
}
