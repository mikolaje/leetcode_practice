"""
Given a linked list, swap every two adjacent nodes
and return its head.
For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.
Your algorithm should use only constant space.
You may not modify the values in the list,
only nodes itself can be changed.
"""


class Node:
    def __init__(self, x=0):
        self.val = x
        self.next = None


def swapPairs(self, head):
    """
    :type head: Node
    :rtype: Node
    """
    if not head or not head.next:
        return head
        dummpyhead = new_head = Node(0)
    while head and head.next:
        tmp = head.next
        head.next = head.next.next
        tmp.next = head
        dummpyhead.next = tmp
        dummpyhead = head
        head = head.next
    return new_head.next

