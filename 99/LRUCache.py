class LRUCache:

    class DoubleNode:
        def __init__(self,k:int,v:int):
            self.key = k
            self.val = v
            self.prev = None
            self.next = None
    class DoubleList:
        def __init__(self):
            self.head = None
            self.tail = None
        
        def add_node(self,new_node):
            if not new_node:
                return
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node

        def move_to_tail(self,node):
            if node is self.tail:
                return
            if node is self.head:
                self.head = self.head.next
                self.head.prev = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node
        
        def remove_head(self):
            if not self.head:
                return None
            ans = self.head
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = ans.next
                self.head.prev = None
                ans.next = None
            return ans
    
        def remove_head(self):
            if not self.head:
                return None
            ans = self.head
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = ans.next
                self.head.prev = None
                ans.next = None
            return ans

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.nodes = self.DoubleList()


    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.nodes.move_to_tail(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.nodes.move_to_tail(node)
        else:
            if len(self.map) == self.capacity:
                removed = self.nodes.remove_head()
                if removed:
                    self.map.pop(removed.key)
            new_node = self.DoubleNode(key,value)
            self.map[key] = new_node
            self.nodes.add_node(new_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)