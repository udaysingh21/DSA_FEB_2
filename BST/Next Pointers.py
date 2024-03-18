"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None: return None
        q=[root]

        while len(q)!=0:
            n=len(q) # tells how many elements in each level
            for i in range(n):
                rn=q.pop(0)
                if i==n-1:
                    rn.next=None
                else:
                    rn.next=q[0]

                if rn.left is not None: q.append(rn.left)
                if rn.right is not None: q.append(rn.right)

        return root