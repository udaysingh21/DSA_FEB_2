# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self,root,p,q):
        if root is None: return None

        if root.val == p or root.val==q: return root

        left=self.helper(root.left,p,q)
        right=self.helper(root.right,p,q)

        if left is None: return right
        if right is None: return left
        return root

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.helper(root,p,q)