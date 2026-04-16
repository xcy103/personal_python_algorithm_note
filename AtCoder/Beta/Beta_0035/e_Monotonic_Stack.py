import sys
n = int(sys.stdin.readline().strip())
arr = list(map(int,sys.stdin.readline().split()))
st = []
res = [0]*n
op = 0
for i,h in enumerate(arr):
    while st and arr[st[-1]]<=h:#注意是小于等于
        st.pop()
    op+=len(st)
    st.append(i)
print(op)