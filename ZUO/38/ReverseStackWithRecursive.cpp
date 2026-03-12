//只用递归，O(1)空间逆序栈
#include<bits/stdc++.h>
using namespace std;


//注意，其实这里，把最后一个元素送出去了，没有压栈
int bottomOut(stack<int> &st){
    int ans = st.top();
    st.pop();
    if(st.empty()) return ans;
    int last = bottomOut(st);
    st.push(ans);
    return last;
}

void reverseStack(stack<int> &st){
    if (st.empty()) return; 
    int num = bottomOut(st);
    reverseStack(st);
    st.push(num);
}