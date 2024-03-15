class Solution:
    # Function to convert a binary tree into its mirror tree.
    def helper(self, root):
        if root is None: return

        # a,b=b,a
        left = self.helper(root.right)
        right = self.helper(root.left)

        root.left, root.right = left, right
        return root

    def mirror(self, root):
        # Code here
        self.helper(root)