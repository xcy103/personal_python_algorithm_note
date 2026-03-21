
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return

    ptr = 0
    n,m = map(int, input_data[ptr:ptr+2])
    ptr += 2

    # 3. 静态数组模拟内存池
    # 空间预估：操作数 m * log(n) * 2。1000 * 31 * 2 = 62000，取 80005 足够。
    limit = 80005
    left = [0] * limit
    right = [0] * limit
    sum_tree = [0] * limit
    add_tag = [0] * limit

    cnt = [1]

    def lazy(i,v,n):
        sum_tree[i] += v * n
        add_tag[i] += v
    
    def down(i,ln,rn):
        if add_tag[i]:
            if left[i]==0:
                cnt[0]+=1
                left[i] = cnt[0]
            if right[i]==0:
                cnt[0]+=1
                right[i] = cnt[0]
            v = add_tag[i]
            lazy(left[i], v, ln)
            lazy(right[i], v, rn)
            add_tag[i] = 0
    
    def update(jobl,jobr,jobv,l,r,i):
        if jobl <= l and r <= jobr:
            lazy(i, jobv, r - l + 1)
        
        else:
            mid = (l + r) >> 1  
            down(i, mid - l + 1, r - mid)
            if jobl <= mid:
                if left[i] == 0:
                    cnt[0] += 1
                    left[i] = cnt[0]
                update(jobl, jobr, jobv, l, mid, left[i])
            if mid < jobr:
                if right[i] == 0:
                    cnt[0] += 1
                    right[i] = cnt[0]
                update(jobl, jobr, jobv, mid + 1, r, right[i])
    
    def query(jobl,jobr,l,r,i):
        if jobl <= l and r <= jobr:
            return sum_tree[i]
        
        else:
            mid = (l + r) >> 1
            down(i, mid - l + 1, r - mid)
            ans = 0
            if jobl <= mid:
                if left[i]:
                    ans += query(jobl, jobr, l, mid, left[i])
            if mid < jobr:
                if right[i]:
                    ans += query(jobl, jobr, mid + 1, r, right[i])
            return ans 

    results = []
    for _ in range(m):                   
        op = int(input_data[ptr])
        if op==1:
            l  = int(input_data[ptr+1]) 
            r  = int(input_data[ptr+2]) 
            v  = int(input_data[ptr+3])
            ptr+=4
            update(l, r, v, 1, n, 1)
        else:
            l  = int(input_data[ptr+1])
            r  = int(input_data[ptr+2])
            ptr+=3
            results.append(str(query(l, r, 1, n, 1)))

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()