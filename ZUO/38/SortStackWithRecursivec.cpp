#include<bits/stdc++.h>
using namespace std;

int deep(stack<int> &st){
    if(st.empty()) return 0;

    int num = st.top();
    st.pop();
    int d = deep(st) + 1;
    st.push(num);
    return d;
}

int maxValue(stack<int> &st,int d){
    if(d==0) return INT_MIN;
    int cur = st.top();
    st.pop();
    int rest = maxValue(st,d-1);
    int ans = cur > rest ? cur : rest;
    st.push(cur);
    return ans;
}

int times(stack<int> &st,int mx,int d){
    if(st.empty()) return 0;
    int cur = st.top();
    st.pop();
    int rest = times(st,mx,d-1);
    int ans = cur == mx ? rest + 1 : rest;
    st.push(cur);
    return ans;
}
void down(stack<int>& st,int mx,int k,int d){
    if(st.empty()){
        for(int i=0;i<k;i++){
            st.push(mx);
        }
    }else{
        int cur = st.top();
        st.pop();
        down(st,mx,k,d-1);
        if(cur!=mx) st.push(cur);
    }
}

void sortStack(stack<int> &st){
    int d = deep(st);
    while(d>0){
        int mx = maxValue(st,d);
        int k = times(st,mx,d);
        down(st,mx,k,d);
        d-=k;
    }
}

int main(){
    stack<int> st;
    st.push(-12);
    st.push(40);
    st.push(2);
    st.push(0);
    st.push(-10);
    while(!st.empty()){
        cout<<st.top()<<" ";
        st.pop();
    }
    cout<<endl;
    st.push(-12);
    st.push(40);
    st.push(2);
    st.push(0);
    st.push(-10);
    sortStack(st);
    while(!st.empty()){
        cout<<st.top()<<" ";
        st.pop();
    }
    cout<<endl;
    return 0;
}