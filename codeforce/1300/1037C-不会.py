n = int(input())
a = input()
b = input()

cost = 0
i = 0

while i < n:
    # 如果当前位置不一样，需要处理
    if a[i] != b[i]:
        # 看看能不能和右边相邻的字符进行“高性价比交换”
        if i + 1 < n and a[i+1] != b[i+1] and a[i] != a[i+1]:
            cost += 1
            i += 2  # 一次交换搞定了两个位置，指针直接跳 2 步
        else:
            cost += 1
            i += 1  # 无法交换，只能硬反转当前位，指针走 1 步
    else:
        i += 1  # 这一位本来就相同，直接看下一位

print(cost)