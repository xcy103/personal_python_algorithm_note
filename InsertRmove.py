import random

# 插入、删除和获取随机元素 O(1)
# https://leetcode.cn/problems/insert-delete-getrandom-o1/

class RandomizedSet:

    def __init__(self):
        self.map = {}   # val -> index
        self.arr = []   # 存储所有元素

    def insert(self, val: int) -> bool:
        """插入一个元素，如果已存在返回 False"""
        if val in self.map:
            return False
        self.map[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        """删除一个元素，如果不存在返回 False"""
        if val not in self.map:
            return False
        idx = self.map[val]
        last_val = self.arr[-1]
        # 把最后一个元素放到被删元素位置
        self.arr[idx] = last_val
        self.map[last_val] = idx
        # 删除最后一个元素
        self.arr.pop()
        del self.map[val]
        return True

    def getRandom(self) -> int:
        """随机返回一个元素"""
        return random.choice(self.arr)
