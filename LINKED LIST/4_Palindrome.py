# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        middle=self.middle(head)
        prev=self.reverse(middle)

        curr=head
        while prev!=None:
            if curr.data!=prev.data:
                return False
            else:
                curr=curr.next
                prev=prev.next

        return True