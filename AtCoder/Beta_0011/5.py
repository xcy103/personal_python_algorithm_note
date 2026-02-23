# 倒推01背包，还不太会
import sys
import operator

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    A = [0] * (N + 1)
    B = [0] * (N + 1)
    
    idx = 2
    for i in range(1, N + 1):
        A[i] = int(input_data[idx])
        B[i] = int(input_data[idx+1])
        idx += 2
        
    dp_pref = [[0] * (M + 1) for _ in range(N + 2)]
    for i in range(1, N + 1):
        w_i = A[i]
        v_i = B[i]
        prev = dp_pref[i-1]
        curr = prev[:]
        for w in range(w_i, M + 1):
            val = prev[w-w_i] + v_i
            if val > curr[w]:
                curr[w] = val
        dp_pref[i] = curr
        
    dp_suff = [[0] * (M + 1) for _ in range(N + 2)]
    for i in range(N, 0, -1):
        w_i = A[i]
        v_i = B[i]
        nxt = dp_suff[i+1]
        curr = nxt[:]
        for w in range(w_i, M + 1):
            val = nxt[w-w_i] + v_i
            if val > curr[w]:
                curr[w] = val
        dp_suff[i] = curr
        
    MAX_V = dp_pref[N][M]
    
    ans = []
    for i in range(1, N + 1):
        w_i = A[i]
        v_i = B[i]
        rem_w = M - w_i
        if rem_w < 0:
            ans.append("No")
            continue
            
        pref = dp_pref[i-1]
        suff = dp_suff[i+1]
        
        max_val = max(map(operator.add, pref[:rem_w+1], suff[rem_w::-1])) + v_i
        
        if max_val == MAX_V:
            ans.append("Yes")
        else:
            ans.append("No")
            
    sys.stdout.write('\n'.join(ans) + '\n')

if __name__ == '__main__':
    solve()
