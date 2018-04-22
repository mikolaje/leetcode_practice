"""
Given a binary tree, return the level order traversal of
its nodes' values. (ie, from left to right, level by level).
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""


def level_queue(root):
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