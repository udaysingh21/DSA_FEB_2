# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, p, q):
        if p is None and q is None: return True

        if p is None and q is not None: return False
        if p is not None and q is None: return False

        if p.val != q.val: return False

        return self.helper(p.left, q.right) and self.helper(p.right, q.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None: return None
        return self.helper(root.left, root.right)
