# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        prev=None

        # a=b b=c c=d d=a

        while curr is not None:
            temp=curr.next # saving next node
            curr.next=prev # reversing curr node
            prev=curr
            curr=temp

        return prev      