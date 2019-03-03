# coding=u8


class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class BST:
    def __init__(self, node_list):
        assert len(node_list) > 0
        self.root = Node(node_list[0])
        for data in node_list[1:]:
            self.insert(data)

    def search(self, node, parent, data):
        if node is None:
            return False, node, parent
        if node.data == data:
            return True, node, parent
        if node.data > data:
            return self.search(node.lchild, node, data)
        else:
            return self.search(node.rchild, node, data)

    # 插入
    def insert(self, data):
        flag, n, p = self.search(self.root, self.root, data)
        if not flag:
            new_node = Node(data)
            if data > p.data:
                p.rchild = new_node
            else:
                p.lchild = new_node

    def is_bst(self):
        self.arr = []
        self.inOrderTraverse(self.root)
        print(self.arr)
        if self.arr==sorted(self.arr):
            return True
        else:
            return False


    def inOrderTraverse(self, node):
        if node:
            self.inOrderTraverse(node.lchild)
            self.arr.append(node.data)
            print (node.data)
            self.inOrderTraverse(node.rchild)

def is_arr_bst(arr):
    """
    如果中序遍历出来的是有序数组那它就是BST
    :param arr:
    :return: BOOL
    """
    def array2bst(arr):
        if not arr:
            return None
        mid = len(arr) // 2
        node = Node(arr[mid])
        node.left = array2bst(arr[:mid])
        node.right = array2bst(arr[mid + 1:])
        return node

    traverse_list = []

    def traverse(node):
        if node:
            traverse(node.lchild)
            traverse_list.append(node.data)
            traverse(node.rchild)

    node = array2bst(arr)
    traverse(node)
    if traverse_list == sorted(arr):
        return True

    return False



a = [49, 38, 65, 97, 60, 76, 13, 27, 5, 1]
bst = BST(a)  # 创建二叉查找树

print(is_arr_bst(a))

#print(bst.is_bst())