# coding=u8

class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None


def removeDups(head):
    """
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    hashset = set()
    prev = Node()

    while head:
        if head.val in hashset:
            prev.next = head.next
        else:
            hashset.add(head.val)
            prev = head
        head = head.next

a1 = Node("A")
a2 = Node("A")
b = Node("B")
c = Node("C")

a1.next=a2
a2.next=b
b.next=c

removeDups(a1)