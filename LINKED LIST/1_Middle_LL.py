# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self, head):
        l = 0
        curr = head

        while curr is not None:
            l += 1
            curr = curr.next

        return l

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = self.length(head)
        counter = l // 2

        curr = head
        while counter != 0:
            curr = curr.next
            counter -= 1

        return curr

    def middleNode1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast,slow=head,head

        #   even length LL and odd length LL
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next

        return slow

