class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def morris(root):
    cur = head
    mostRight = None
    while cur:
        mostRight = cur.left
        if mostRight:
            while mostRight.right and mostRight.right != cur:
                mostRight = mostRight.right
        
            if mostRight.right == None:
                mostRight.right = cur
                cur = cur.left
                print(cur.val)
                continue
            else:
                mostRight.right = None

        cur = cur.right

def morrisPreorder(head, ans):
    cur = head
    mostRight = None
    while cur:
        mostRight = cur.left
        if mostRight: # cur有左树
            # 找到左树最右节点
            # 注意左树最右节点的右指针可能指向空，也可能指向cur
            while mostRight.right and mostRight.right != cur:
                mostRight = mostRight.right
            
            # 判断左树最右节点的右指针状态
            if mostRight.right is None: # 第一次到达
                ans.append(cur.val)
                mostRight.right = cur
                cur = cur.left
                continue
            else: # 第二次到达
                mostRight.right = None
        else: # cur无左树
            ans.append(cur.val)
            
        cur = cur.right

def morrisInorder(head, ans):
    cur = head
    mostRight = None
    while cur:
        mostRight = cur.left
        if mostRight: # cur有左树
            # 找到左树最右节点
            # 注意左树最右节点的右指针可能指向空，也可能指向cur
            while mostRight.right and mostRight.right != cur:
                mostRight = mostRight.right
            
            # 判断左树最右节点的右指针状态
            if mostRight.right is None: # 第一次到达
                mostRight.right = cur
                cur = cur.left
                continue
            else: # 第二次到达
                mostRight.right = None
        
        ans.append(cur.val)
        cur = cur.right


def morrisPostorder(head, ans):
    cur = head
    mostRight = None
    while cur:
        mostRight = cur.left
        if mostRight: # cur有左树
            # 找到左树最右节点
            # 注意左树最右节点的右指针可能指向空，也可能指向cur
            while mostRight.right and mostRight.right != cur:
                mostRight = mostRight.right
            
            # 判断左树最右节点的右指针状态
            if mostRight.right is None: # 第一次到达
                mostRight.right = cur
                cur = cur.left
                continue
            else: # 第二次到达
                mostRight.right = None
                # 输出左树
                collect(cur.left, ans)

        cur = cur.right
    collect(cur, ans)   

def collect(head, ans):
    tail = reverse(head)
    cur = tail
    while cur:
        ans.append(cur.val)
        cur = cur.right
    reverse(tail)

def reverse(head):
    pre = None
    cur = head
    while cur:
        next = cur.right
        cur.right = pre
        pre = cur
        cur = next
    return pre

