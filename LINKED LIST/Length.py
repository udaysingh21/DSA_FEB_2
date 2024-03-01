'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


def length(head):
    l=0

    curr=head
    while curr is not None:
        l+=1
        curr=curr.next

    return l