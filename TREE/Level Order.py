# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        q=[]
        q.append(root)
        ans=[]

        while len(q)!=0:
            n=len(q) # no of elements in particular level
            sub=[]
            for i in range(n):
                rn=q.pop(0)
                sub.append(rn.val)

                if rn.left is not None:
                    q.append(rn.left)

                if rn.right is not None:
                    q.append(rn.right)

            ans.append(sub)

        return ans