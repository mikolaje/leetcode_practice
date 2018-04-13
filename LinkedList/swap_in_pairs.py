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


def swapPairs1(self, head):
    """
    :type head: Node
    :rtype: Node
    """
    if not head or not head.next:
        return head

    dummyhead = new_head = Node(0)
    while head and head.next:
        tmp = head.next
        head.next = head.next.next  # 要把赋值 x.next看成给x 指引的意思。它指引到下一个node
        tmp.next = head
        dummyhead.next = tmp
        dummyhead = head
        head = head.next
    return new_head.next


def swapPairs2(head):

    if head and head.next:
        # 和reverse差不多也是一个接着一个
        tmp = head.next
        head.next = swapPairs2(tmp.next)
        tmp.next = head
        return tmp
    return head

