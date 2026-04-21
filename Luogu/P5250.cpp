/*
Author: yangka
Date: 2026-04-18 14:13:09
*/

#include <bits/stdc++.h>
#define ll long long
using namespace std;
set<ll> s;


int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin>>n;
    while(n--){
        int op;
        ll l;
        cin>>op>>l;
        if(op==1){
            if(s.count(l)){
                cout << "Already Exist\n";
            }else{
                s.insert(l);
            }
        }else{
            if (s.empty()) {
                cout << "Empty\n";
                continue;
            }
            auto it = s.lower_bound(l);
            if(it==s.begin()){
                cout<<*it<<'\n';
                s.erase(it);
            }
            else if(it==s.end()){
                auto pre = prev(it);
                cout<<*pre<<'\n';
                s.erase(pre);
            }else{
                auto right = it;
                auto left = prev(it);
                if (abs(*left - l) <= abs(*right - l)) {
                    cout << *left << '\n';
                    s.erase(left);
                } else {
                    cout << *right << '\n';
                    s.erase(right);
                }
            }
        }
    }
    

    return 0;
}