import sys
#就是一个转化问题，区间最大重合
def solve():
    # 使用快速读取
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    
    events = []
    idx = 2
    for _ in range(n):
        l_i = int(input_data[idx])
        r_i = int(input_data[idx+1])
        idx += 2
        
        # 转化后的区间是 [l_i - k, r_i]
        # 事件格式：(坐标, 类型)
        # 类型：+1 表示区间开始，-1 表示区间结束
        # 为了处理闭区间相交，同一位置先处理 +1，后处理 -1
        events.append((l_i - k, 1))
        events.append((r_i, -1))
    
    # 按照坐标排序
    # 如果坐标相同，先处理 1 (进入)，再处理 -1 (离开)
    # Python 的 sort 是稳定的，或者直接把类型 1 设为较大权重，或者像下面这样写
    events.sort(key=lambda x: (x[0], -x[1]))
    
    max_intersect = 0
    current_count = 0
    
    for _, type in events:
        current_count += type
        if current_count > max_intersect:
            max_intersect = current_count
            
    print(max_intersect)

if __name__ == "__main__":
    solve()