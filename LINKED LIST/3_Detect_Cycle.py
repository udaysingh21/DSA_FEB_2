# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes=set()

        curr=head
        while curr is not None:
            if curr in nodes:
                return curr
            else:
                nodes.add(curr)
                curr=curr.next

        return None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1:
    def cycle(self,head):
        fast,slow=head,head

        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                return fast

        return -1

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans=self.cycle(head)
        if ans==-1: return None
        slow=head
        fast=ans # fast

        while fast!=slow:
            fast=fast.next
            slow=slow.next

        return fast