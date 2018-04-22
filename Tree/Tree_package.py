# coding=u8
"""
author: https://blog.csdn.net/bone_ace/article/details/46718683
"""

class Node(object):
    def __init__(self,elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, elem):
        node = Node(elem)
        if self.root.elem == -1:  # 如果树是空的，则对根节点赋值
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)


    def front_digui(self, root):
        if root == None:
            return
        print (root.elem)
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)

    def middle_digui(self, root):
        if root == None:
            return
        self.middle_digui(root.lchild)
        print (root.elem)
        self.middle_digui(root.rchild)


    def later_digui(self, root):
        if root == None:
            return
        self.later_digui(root.lchild)
        self.later_digui(root.rchild)
        print(root.elem)


    def front_stack(self, root):
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:
                print(node.elem)
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()
            node = node.rchild

    def middle_stack(self, root):
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()
            print(node.elem)
            node = node.rchild

    def later_stack(self, root):
        if root == None:
            return
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        while myStack1:
            node = myStack1.pop()
            if node.lchild:
                myStack1.append(node.lchild)
            if node.rchild:
                myStack1.append(node.rchild)
            myStack2.append(node)

    def level_queue(self, root):
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.elem)
            if node.lchild:
                myQueue.append(node.lchild)
            if node.rchild:
                myQueue.append(node.rchild)


if __name__=='__main__':
    elems = range(10)
    tree = Tree()
    for elem in elems:
        tree.add(elem)

    #tree.level_queue(tree.root)

    #tree.front_digui(tree.root)

    #tree.middle_digui(tree.root)

    tree.later_digui(tree.root)