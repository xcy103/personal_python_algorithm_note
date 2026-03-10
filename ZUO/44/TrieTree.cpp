#include<bits/stdc++.h>
using namespace std;
const int MAXN = 150001;

int tree[MAXN][26],p[MAXN],e[MAXN],cnt;

void build(){
    cnt = 1;
}
void insert_word(const string& word){
    int cur = 1;
    p[cur]++;
    for(char c:word){
        int path = c-'a';
        if(tree[cur][path]==0){
            tree[cur][path] = ++cnt;
        }
        cur = tree[cur][path];
        p[cur]++;
    }
    e[cur]++;
}
int  search_word(const string& word){ 
    int cur = 1;
    for(char c:word){
        int path = c-'a';
        if(tree[cur][path]==0){
            return 0;
        }
        cur = tree[cur][path];
    }
    return e[cur];//注意这里必须是return e因为必须是结尾
}   

int prefixNumber(const string& word){ 
    int cur = 1;
    for(char c:word){
        int path = c-'a';
        if(tree[cur][path]==0){
            return 0;
        }
        cur = tree[cur][path];
    }
    return p[cur];//注意这里必须是return p因为必须是前缀
}

void delete_word(const string& word){ 
    if(search_word(word)){
        int cur = 1;
        p[cur]--;
        for(char c:word){
            int path = c-'a';
            if(--p[tree[cur][path]]==0){
                tree[cur][path] = 0;
                return;
                //为什么这里可以直接返回
                //因为如果我们来到p，发现-1之后为0，说明后面的部分只出现过一次
                //我们可以直接把tree[cur][path]置0，这样相当于把p和e的这一位都舍弃了
                //因为cnt不回退
            }
            cur = tree[cur][path];
        }
        e[cur]--;
    }
}
void clear(){
    for(int i=1;i<=cnt;i++){
        memset(tree[i],0,sizeof(tree[i]));
        p[i] = e[i] = 0;
    }
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int m,op;
    string word;
    while(cin>>m){
        build();
        for(int i=1;i<=m;i++){
            cin>>op>>word;
            if (op == 1) {
                insert_word(word);
            } else if (op == 2) {
                delete_word(word);
            } else if (op == 3) {
                cout << (search_word(word) > 0 ? "YES" : "NO") << '\n';
            } else if (op == 4) {
                cout << prefixNumber(word) << '\n';
            }
        }
        clear();
    }
    return 0;
}

