#  两个0和1数量相等区间的最大长度
#  给出一个长度为n的01串，现在请你找到两个区间
#  使得这两个区间中，1的个数相等，0的个数也相等
#  这两个区间可以相交，但是不可以完全重叠，即两个区间的左右端点不可以完全一样
#  现在请你找到两个最长的区间，满足以上要求
#  返回区间最大长度
#  来自真实大厂笔试，没有在线测试，对数器验证

def len2(arr):
    left_zero = -1
    right_zero = -1
    left_one = -1
    right_one = -1

    # 找最左 0
    for i in range(len(arr)):
        if arr[i] == 0:
            left_zero = i
            break

    # 找最左 1
    for i in range(len(arr)):
        if arr[i] == 1:
            left_one = i
            break

    # 找最右 0
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == 0:
            right_zero = i
            break

    # 找最右 1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == 1:
            right_one = i
            break

    p1 = right_zero - left_zero
    p2 = right_one - left_one

    return max(p1, p2)