import sys

n,m = map(int,input().split())
s = list(input())

t = (n-m)//2

st = []
for i,ch in enumerate(s):
    if ch=='(':
        st.append(ch)
    else:
        if t>0:
            st.pop()
            t-=1
        else:
            st.append(ch)
print(''.join(st))