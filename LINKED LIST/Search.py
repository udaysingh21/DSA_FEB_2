"""
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

"""


def searchInLinkedList(head, k):
# Your code goes here.
    curr=head
    while curr is not None:
        if curr.data==k:
            return True
        else:
            curr=curr.next

    return -1