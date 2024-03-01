class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Do not change code above.


def insertAtFirst(head: Node, newValue: int) -> Node:
    # Write your code here
    n=Node(newValue)
    n.next=head

    # n is the new head because now it is in beginning

    return n