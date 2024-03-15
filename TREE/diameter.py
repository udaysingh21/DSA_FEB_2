# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Diameter aka Maximum width of Binary Tree
    # It is defined as no. of nodes in largest path between any 2 leaf nodes
    def height(self,root):
        # height of single node is taken as 0
        if root is None: return 0

        lh=self.height(root.left)
        rh=self.height(root.right)

        self.diameter=max(self.diameter,lh+rh)
        return 1+max(lh,rh)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0
        self.height(root)
        return self.diameter