# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None: return None
        maxi=max(p.val,q.val) #  p=max(p.val,q.val) p=int
        mini=min(p.val,q.val)

        while root:
            if root.val>maxi: root=root.left
            elif root.val<mini: root=root.right
            else:
                return root

        return None