"""
Write a function to delete a node (except the tail)
in a singly linked list, given only access to that node.
Supposed the linked list is 1 -> 2 -> 3 -> 4 and
you are given the third node with value 3,
the linked list should become 1 -> 2 -> 4 after calling your function.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)

node3 = Node(3)
node2 = Node(2)
node2.next = node3
node1 = Node(1)
node1.next = node2

head = node1

def delete_node(node):
    node.val = node.next
    node.next = node.next.next

if __name__ == '__main__':
    delete_node(node2)
    while head:
        print(head)
        head = head.next

