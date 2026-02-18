import sys

map_data = {}
setAllTime = -1
setAllValue = 0
cnt = 0

def put(k, v):
    global cnt
    map_data[k] = (v, cnt)
    cnt += 1

def setAll(v):
    global setAllTime, setAllValue, cnt
    setAllTime = cnt  # ✅ 修复大小写错误
    setAllValue = v
    cnt += 1

def get(k):
    global map_data, setAllTime
    if k not in map_data:
        return -1
    value, time = map_data[k]
    if time > setAllTime:   # ✅ 判断条件修正
        return value
    else:
        return setAllValue

def main():
    global cnt, setAllTime, setAllValue, map_data
    data = sys.stdin.read().strip().split()
    idx = 0
    out = []
    while idx < len(data):
        map_data.clear()
        setAllTime = -1
        setAllValue = 0
        cnt = 0
        n = int(data[idx]); idx += 1
        for _ in range(n):
            op = int(data[idx]); idx += 1
            if op == 1:  # put
                k = int(data[idx]); idx += 1
                v = int(data[idx]); idx += 1
                put(k, v)
            elif op == 2:  # get
                k = int(data[idx]); idx += 1
                out.append(str(get(k)))
            else:  # setAll
                v = int(data[idx]); idx += 1
                setAll(v)
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
