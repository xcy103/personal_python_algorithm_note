
import sys

MAXN = 500005
LOWEST = -float('inf')

arr = [0] * MAXN
sum_t = [0] * (MAXN << 2)
max_t = [0] * (MAXN << 2)
cnt_t = [0] * (MAXN << 2)
sem_t = [0] * (MAXN << 2)
max_h = [0] * (MAXN << 2)

#懒标记
max_add = [0] * (MAXN << 2)
other_add = [0] * (MAXN << 2)
max_atp = [0] * (MAXN << 2)
other_atp = [0] * (MAXN << 2)

def up(i):
    l,r = i<<1,i<<1|1
    sum_t[i] = sum_t[l] + sum_t[r]
    max_h[i] = max(max_h[l], max_h[r])
    max_t[i] = max(max_t[l], max_t[r])

    if max_t[l] > max_t[r]:
        cnt_t[i] = cnt_t[l]
        sem_t[i] = max(sem_t[l], max_t[r])
    elif max_t[l] < max_t[r]:
        cnt_t[i] = cnt_t[r]
        sem_t[i] = max(max_t[l], sem_t[r])
    else:
        cnt_t[i] = cnt_t[l] + cnt_t[r]
        sem_t[i] = max(sem_t[l], sem_t[r])

def lazy(i,n,max_add,other_add,max_up,other_up):
    max_h[i] = max(max_h[i], max_up+max_t[i])
    max_atp[i]