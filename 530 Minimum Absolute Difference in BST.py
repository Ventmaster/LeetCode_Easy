# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        previous = float('-inf')
        minimum_difference = float('inf')

        def inordertraversal(root):
            nonlocal previous, minimum_difference

            if not root:
                return 

            if root.left:
                inordertraversal(root.left)

            if (root.val - previous) < minimum_difference:
                minimum_difference = root.val - previous

            previous = root.val

            if root.right:
                inordertraversal(root.right)

        inordertraversal(root)
        return minimum_difference 
