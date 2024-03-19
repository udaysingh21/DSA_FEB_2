# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, ans):
        if root is None: return

        self.inorder(root.left, ans)
        ans.append(root.val)
        self.inorder(root.right, ans)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        self.inorder(root, ans)
        # [2,2,2]
        n = len(ans)  # 3

        # [2,2,2]==[2,2,2] and 3==1
        if ans == sorted(ans) and n == len(set(ans)):
            return True
        else:
            return False
