class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Please do not change code above.


def deleteLast(head: Node) -> Node:
    # Write your code here
    curr=head
    prev=None

    while curr.next is not None:
        prev=curr
        curr=curr.next

    prev.next=None
    return head
